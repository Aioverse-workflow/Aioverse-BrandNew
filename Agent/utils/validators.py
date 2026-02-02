"""
Utility functions for asset management
Includes metadata, validation, and file handling utilities
"""

import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from ..config import METADATA_SCHEMA, SUPPORTED_FORMATS, TOKEN_CONFIG


class MetadataManager:
    """Handles asset metadata operations"""

    @staticmethod
    def validate_metadata(metadata: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate metadata against schema

        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []

        for field, field_type in METADATA_SCHEMA.items():
            if field in metadata:
                if not isinstance(metadata[field], field_type):
                    errors.append(f"Field '{field}' has invalid type. Expected {field_type.__name__}")

        return len(errors) == 0, errors

    @staticmethod
    def merge_metadata(
        existing: Dict[str, Any], updates: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Merge metadata updates with existing metadata"""
        merged = existing.copy()
        merged.update(updates)
        merged["modified_date"] = datetime.now().isoformat()
        return merged

    @staticmethod
    def generate_metadata_hash(metadata: Dict[str, Any]) -> str:
        """Generate hash of metadata for integrity checking"""
        metadata_str = json.dumps(metadata, sort_keys=True, default=str)
        return hashlib.sha256(metadata_str.encode()).hexdigest()


class FileValidator:
    """Handles file validation for assets"""

    @staticmethod
    def validate_file_format(file_path: str, category: str) -> Tuple[bool, Optional[str]]:
        """
        Validate file format matches category

        Returns:
            Tuple of (is_valid, error_message)
        """
        file_path_obj = Path(file_path)
        file_ext = file_path_obj.suffix.lower()

        if category == "fonts" and file_ext not in SUPPORTED_FORMATS["fonts"]:
            return False, f"Invalid font format: {file_ext}"
        elif category in ["logos", "icons", "illustrations", "photos"]:
            if file_ext not in SUPPORTED_FORMATS["images"]:
                return False, f"Invalid image format: {file_ext}"

        return True, None

    @staticmethod
    def validate_file_size(file_path: str, max_size_mb: int = 100) -> Tuple[bool, Optional[str]]:
        """Validate file size is within limits"""
        file_path_obj = Path(file_path)
        file_size_mb = file_path_obj.stat().st_size / (1024 * 1024)

        if file_size_mb > max_size_mb:
            return False, f"File size {file_size_mb:.2f}MB exceeds limit of {max_size_mb}MB"

        return True, None

    @staticmethod
    def validate_file_integrity(file_path: str) -> Tuple[bool, Optional[str]]:
        """Validate file is readable and not corrupted"""
        try:
            file_path_obj = Path(file_path)
            if not file_path_obj.exists():
                return False, "File does not exist"
            if not file_path_obj.is_file():
                return False, "Path is not a file"
            # Try to read file
            with open(file_path_obj, "rb") as f:
                f.read(1024)  # Read first 1KB
            return True, None
        except Exception as e:
            return False, f"File integrity check failed: {str(e)}"


class TokenGenerator:
    """Generates and validates asset tokens"""

    @staticmethod
    def generate_token(
        prefix: str, family: str, variant: str, sequence_number: int = 1
    ) -> str:
        """Generate a new asset token"""
        if prefix not in TOKEN_CONFIG["prefixes"]:
            raise ValueError(f"Invalid prefix: {prefix}")
        if family not in TOKEN_CONFIG["families"]:
            raise ValueError(f"Invalid family: {family}")

        return f"{prefix}-{family}-{variant}{sequence_number:03d}"

    @staticmethod
    def validate_token(token: str) -> Tuple[bool, Optional[str]]:
        """Validate token format"""
        try:
            parts = token.split("-")
            if len(parts) < 3:
                return False, "Token must have at least 3 parts separated by hyphens"

            prefix = parts[0]
            family = parts[1]
            variant_num = "-".join(parts[2:])

            if prefix not in TOKEN_CONFIG["prefixes"]:
                return False, f"Invalid prefix: {prefix}"

            if family not in TOKEN_CONFIG["families"]:
                return False, f"Invalid family: {family}"

            # Check variant has numeric suffix
            if not any(c.isdigit() for c in variant_num):
                return False, "Token must end with numeric identifier"

            return True, None
        except Exception as e:
            return False, str(e)

    @staticmethod
    def parse_token(token: str) -> Optional[Dict[str, str]]:
        """Parse token into components"""
        valid, error = TokenGenerator.validate_token(token)
        if not valid:
            return None

        parts = token.split("-")
        import re

        # Extract variant and number
        variant_num = "-".join(parts[2:])
        match = re.match(r"^([A-Z]+)(\d+)$", variant_num)

        if not match:
            return None

        return {
            "prefix": parts[0],
            "family": parts[1],
            "variant": match.group(1),
            "number": match.group(2),
            "full_token": token,
        }


class FileHelper:
    """Helper functions for file operations"""

    @staticmethod
    def get_file_hash(file_path: str) -> str:
        """Generate SHA256 hash of file content"""
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

    @staticmethod
    def copy_file(source: str, destination: str, preserve_metadata: bool = True):
        """Copy file from source to destination"""
        source_path = Path(source)
        dest_path = Path(destination)

        if not source_path.exists():
            raise FileNotFoundError(f"Source file not found: {source}")

        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_bytes(source_path.read_bytes())

        if preserve_metadata:
            import shutil

            shutil.copystat(source_path, dest_path)

    @staticmethod
    def list_files_in_directory(directory: str, extension: Optional[str] = None) -> List[Path]:
        """List all files in a directory, optionally filtered by extension"""
        dir_path = Path(directory)
        if not dir_path.exists():
            return []

        files = list(dir_path.glob("*"))
        if extension:
            files = [f for f in files if f.suffix.lower() == extension.lower()]

        return files

    @staticmethod
    def calculate_directory_size(directory: str) -> int:
        """Calculate total size of directory in bytes"""
        total = 0
        for file_path in Path(directory).rglob("*"):
            if file_path.is_file():
                total += file_path.stat().st_size
        return total


class ComplianceChecker:
    """Check asset compliance with brand standards"""

    COMPLIANCE_RULES = {
        "token_format": "Asset must have valid token format",
        "metadata_complete": "Asset must have complete metadata",
        "file_exists": "Asset file must exist on disk",
        "proper_naming": "Asset must follow naming conventions",
        "tagged": "Asset should be properly tagged",
    }

    @staticmethod
    def check_compliance(metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Check if asset meets compliance requirements

        Returns:
            Dictionary with compliance status and issues
        """
        issues = []
        warnings = []

        # Check token format
        if "token" in metadata:
            from .utils import TokenGenerator

            valid, error = TokenGenerator.validate_token(metadata["token"])
            if not valid:
                issues.append(f"Invalid token format: {error}")

        # Check required metadata
        required = ["original_name", "category", "family", "variant"]
        for field in required:
            if field not in metadata or not metadata[field]:
                issues.append(f"Missing required field: {field}")

        # Check file exists
        if "file_path" in metadata:
            if not Path(metadata["file_path"]).exists():
                warnings.append("Asset file does not exist on disk")

        # Check tagging
        if "tags" not in metadata or not metadata["tags"]:
            warnings.append("Asset is not tagged")

        # Check naming convention
        if "standardized_name" in metadata:
            if not metadata["standardized_name"].replace("_", "-"):
                warnings.append("Naming convention not followed")

        return {
            "compliant": len(issues) == 0,
            "issues": issues,
            "warnings": warnings,
            "checked_at": datetime.now().isoformat(),
        }
