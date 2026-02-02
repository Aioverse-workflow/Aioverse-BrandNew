"""
Core Asset Manager Engine
Handles all asset operations: import, export, organize, and refine
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..config import ASSET_PATHS, METADATA_SCHEMA, STORAGE_CONFIG, TOKEN_CONFIG


class AssetManager:
    """Main asset management engine for Aioverse brand assets"""

    def __init__(self):
        """Initialize the Asset Manager"""
        self.logger = logging.getLogger(__name__)
        self.asset_registry: Dict[str, Dict[str, Any]] = {}
        self.metadata_store: Dict[str, Dict[str, Any]] = {}
        self._ensure_storage_directories()
        self._load_existing_data()

    def _ensure_storage_directories(self):
        """Create necessary storage directories"""
        for directory in STORAGE_CONFIG.values():
            if isinstance(directory, Path):
                directory.parent.mkdir(parents=True, exist_ok=True)

    def _load_existing_data(self):
        """Load existing asset metadata and registry from storage"""
        try:
            if STORAGE_CONFIG["metadata_file"].exists():
                with open(STORAGE_CONFIG["metadata_file"], "r") as f:
                    self.metadata_store = json.load(f)
            if STORAGE_CONFIG["registry_file"].exists():
                with open(STORAGE_CONFIG["registry_file"], "r") as f:
                    self.asset_registry = json.load(f)
        except Exception as e:
            self.logger.warning(f"Could not load existing data: {e}")

    def _save_data(self):
        """Persist asset metadata and registry to storage"""
        try:
            with open(STORAGE_CONFIG["metadata_file"], "w") as f:
                json.dump(self.metadata_store, f, indent=2, default=str)
            with open(STORAGE_CONFIG["registry_file"], "w") as f:
                json.dump(self.asset_registry, f, indent=2, default=str)
        except Exception as e:
            self.logger.error(f"Failed to save data: {e}")

    def import_asset(
        self,
        file_path: str,
        token: str,
        category: str,
        family: str,
        variant: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Import a new asset and register it in the system

        Args:
            file_path: Path to the asset file
            token: Unique token (e.g., LOGO-AIOTIZE-PFP001)
            category: Asset category (LOGO, ICON, etc.)
            family: Asset family (AIOTIZE, AIOVERSE, etc.)
            variant: Asset variant (PFP, MARK, etc.)
            metadata: Additional metadata dictionary

        Returns:
            Dictionary containing import result and asset metadata
        """
        file_path_obj = Path(file_path)

        if not file_path_obj.exists():
            raise FileNotFoundError(f"Asset file not found: {file_path}")

        # Generate standardized name
        standardized_name = self._generate_standardized_name(
            file_path_obj.name, token
        )

        # Build asset metadata
        asset_metadata = {
            "token": token,
            "original_name": file_path_obj.name,
            "standardized_name": standardized_name,
            "category": category,
            "family": family,
            "variant": variant,
            "file_path": str(file_path_obj),
            "file_size": file_path_obj.stat().st_size,
            "created_date": datetime.now().isoformat(),
            "modified_date": datetime.now().isoformat(),
            "version": "1.0",
            "tags": metadata.get("tags", []) if metadata else [],
            "description": metadata.get("description", "") if metadata else "",
            "usage_rights": metadata.get("usage_rights", "") if metadata else "",
        }

        # Store asset metadata
        self.metadata_store[token] = asset_metadata
        self.asset_registry[token] = {
            "status": "active",
            "indexed": True,
            "last_accessed": datetime.now().isoformat(),
        }

        self._save_data()
        self.logger.info(f"Asset imported successfully: {token}")

        return {"success": True, "token": token, "metadata": asset_metadata}

    def export_asset(
        self, token: str, export_path: str, include_metadata: bool = True
    ) -> Dict[str, Any]:
        """
        Export an asset with optional metadata

        Args:
            token: Asset token to export
            export_path: Destination path for export
            include_metadata: Whether to include metadata JSON

        Returns:
            Dictionary containing export result
        """
        if token not in self.metadata_store:
            raise ValueError(f"Asset not found: {token}")

        metadata = self.metadata_store[token]
        source_file = Path(metadata["file_path"])

        if not source_file.exists():
            raise FileNotFoundError(f"Source file not found: {source_file}")

        export_path_obj = Path(export_path)
        export_path_obj.mkdir(parents=True, exist_ok=True)

        # Copy asset file
        dest_file = export_path_obj / metadata["standardized_name"]
        dest_file.write_bytes(source_file.read_bytes())

        result = {
            "success": True,
            "token": token,
            "exported_file": str(dest_file),
            "file_size": dest_file.stat().st_size,
        }

        # Export metadata if requested
        if include_metadata:
            metadata_file = export_path_obj / f"{token}_metadata.json"
            with open(metadata_file, "w") as f:
                json.dump(metadata, f, indent=2, default=str)
            result["metadata_file"] = str(metadata_file)

        self.logger.info(f"Asset exported: {token} to {export_path}")
        return result

    def organize_assets(
        self, organization_method: str = "by_category"
    ) -> Dict[str, Any]:
        """
        Organize assets based on specified method

        Args:
            organization_method: 'by_category', 'by_family', 'by_status'

        Returns:
            Dictionary containing organized asset structure
        """
        organized = {}

        if organization_method == "by_category":
            for token, metadata in self.metadata_store.items():
                category = metadata.get("category", "uncategorized")
                if category not in organized:
                    organized[category] = []
                organized[category].append(
                    {"token": token, "name": metadata.get("standardized_name")}
                )

        elif organization_method == "by_family":
            for token, metadata in self.metadata_store.items():
                family = metadata.get("family", "uncategorized")
                if family not in organized:
                    organized[family] = []
                organized[family].append(
                    {"token": token, "name": metadata.get("standardized_name")}
                )

        elif organization_method == "by_status":
            for token, registry in self.asset_registry.items():
                status = registry.get("status", "unknown")
                if status not in organized:
                    organized[status] = []
                organized[status].append(token)

        self.logger.info(f"Assets organized by {organization_method}")
        return {
            "success": True,
            "method": organization_method,
            "organization": organized,
            "total_assets": len(self.metadata_store),
        }

    def refine_asset(
        self, token: str, refinement_type: str, parameters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Apply refinements to an asset

        Args:
            token: Asset token to refine
            refinement_type: Type of refinement (compress, optimize, convert, enhance)
            parameters: Refinement parameters

        Returns:
            Dictionary containing refinement result
        """
        if token not in self.metadata_store:
            raise ValueError(f"Asset not found: {token}")

        metadata = self.metadata_store[token]

        refinement_record = {
            "type": refinement_type,
            "parameters": parameters,
            "timestamp": datetime.now().isoformat(),
            "status": "applied",
        }

        if "refinements" not in metadata:
            metadata["refinements"] = []

        metadata["refinements"].append(refinement_record)
        metadata["modified_date"] = datetime.now().isoformat()

        self._save_data()
        self.logger.info(f"Asset refined: {token} with {refinement_type}")

        return {
            "success": True,
            "token": token,
            "refinement_type": refinement_type,
            "result": refinement_record,
        }

    def validate_asset(self, token: str) -> Dict[str, Any]:
        """
        Validate asset compliance with Aioverse standards

        Args:
            token: Asset token to validate

        Returns:
            Dictionary containing validation results
        """
        if token not in self.metadata_store:
            raise ValueError(f"Asset not found: {token}")

        metadata = self.metadata_store[token]
        validation_results = {
            "token": token,
            "issues": [],
            "warnings": [],
            "compliant": True,
        }

        # Validate token format
        if not self._validate_token_format(token):
            validation_results["issues"].append("Invalid token format")
            validation_results["compliant"] = False

        # Validate required metadata
        required_fields = ["original_name", "category", "family", "variant"]
        for field in required_fields:
            if field not in metadata or not metadata[field]:
                validation_results["issues"].append(f"Missing required field: {field}")
                validation_results["compliant"] = False

        # Validate file existence
        if not Path(metadata.get("file_path", "")).exists():
            validation_results["warnings"].append("Source file not found")

        self.logger.info(f"Asset validated: {token}, compliant={validation_results['compliant']}")
        return validation_results

    def search_assets(
        self, query: str, search_type: str = "token"
    ) -> List[Dict[str, Any]]:
        """
        Search for assets in the registry

        Args:
            query: Search query
            search_type: 'token', 'name', 'category', 'tag'

        Returns:
            List of matching assets
        """
        results = []

        for token, metadata in self.metadata_store.items():
            match = False

            if search_type == "token" and query.upper() in token.upper():
                match = True
            elif search_type == "name" and query.lower() in metadata.get(
                "standardized_name", ""
            ).lower():
                match = True
            elif search_type == "category" and metadata.get("category") == query:
                match = True
            elif search_type == "tag" and query in metadata.get("tags", []):
                match = True

            if match:
                results.append({"token": token, "metadata": metadata})

        self.logger.info(f"Search completed: {len(results)} results for '{query}'")
        return results

    def get_asset_info(self, token: str) -> Dict[str, Any]:
        """Get complete information about an asset"""
        if token not in self.metadata_store:
            raise ValueError(f"Asset not found: {token}")

        return {
            "metadata": self.metadata_store[token],
            "registry": self.asset_registry.get(token, {}),
        }

    def _generate_standardized_name(self, original_name: str, token: str) -> str:
        """Generate standardized asset name"""
        file_ext = Path(original_name).suffix
        return f"{token}{file_ext}".replace("-", "_")

    def _validate_token_format(self, token: str) -> bool:
        """Validate token format: PREFIX-FAMILY-VARIANT###"""
        parts = token.split("-")
        if len(parts) < 3:
            return False

        prefix, family, variant_num = parts[0], parts[1], "-".join(parts[2:])

        # Check prefix
        if prefix not in TOKEN_CONFIG["prefixes"]:
            return False

        # Check family
        if family not in TOKEN_CONFIG["families"]:
            return False

        return True

    def get_statistics(self) -> Dict[str, Any]:
        """Get overall statistics about the asset collection"""
        categories = {}
        families = {}
        total_size = 0

        for metadata in self.metadata_store.values():
            category = metadata.get("category", "unknown")
            family = metadata.get("family", "unknown")
            file_size = metadata.get("file_size", 0)

            categories[category] = categories.get(category, 0) + 1
            families[family] = families.get(family, 0) + 1
            total_size += file_size

        return {
            "total_assets": len(self.metadata_store),
            "by_category": categories,
            "by_family": families,
            "total_size_bytes": total_size,
            "total_size_mb": round(total_size / (1024 * 1024), 2),
        }
