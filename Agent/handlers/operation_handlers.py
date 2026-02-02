"""
Operation handlers for specific asset management tasks
"""

import logging
from pathlib import Path
from typing import Any, Dict, Optional

from ..core import AssetManager
from ..utils import ComplianceChecker, FileHelper, FileValidator, TokenGenerator


class ImportHandler:
    """Handles asset import operations"""

    def __init__(self, asset_manager: AssetManager):
        self.asset_manager = asset_manager
        self.logger = logging.getLogger(__name__)

    def handle_import(
        self,
        file_path: str,
        token: str,
        category: str,
        family: str,
        variant: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Handle asset import with validation
        """
        # Validate token
        valid, error = TokenGenerator.validate_token(token)
        if not valid:
            return {"success": False, "error": f"Invalid token: {error}"}

        # Validate file format
        valid, error = FileValidator.validate_file_format(file_path, category)
        if not valid:
            return {"success": False, "error": error}

        # Validate file size
        valid, error = FileValidator.validate_file_size(file_path)
        if not valid:
            return {"success": False, "error": error}

        # Validate file integrity
        valid, error = FileValidator.validate_file_integrity(file_path)
        if not valid:
            return {"success": False, "error": error}

        # Perform import
        return self.asset_manager.import_asset(
            file_path, token, category, family, variant, metadata
        )


class ExportHandler:
    """Handles asset export operations"""

    def __init__(self, asset_manager: AssetManager):
        self.asset_manager = asset_manager
        self.logger = logging.getLogger(__name__)

    def handle_export(
        self,
        token: str,
        export_path: str,
        include_metadata: bool = True,
        include_compliance: bool = True,
    ) -> Dict[str, Any]:
        """Handle asset export with compliance info"""
        if include_compliance:
            # Get asset info
            try:
                asset_info = self.asset_manager.get_asset_info(token)
                metadata = asset_info["metadata"]

                # Check compliance
                compliance = ComplianceChecker.check_compliance(metadata)
            except ValueError:
                return {"success": False, "error": f"Asset not found: {token}"}

        # Perform export
        result = self.asset_manager.export_asset(token, export_path, include_metadata)

        if include_compliance:
            result["compliance"] = compliance

        return result


class OrganizeHandler:
    """Handles asset organization operations"""

    def __init__(self, asset_manager: AssetManager):
        self.asset_manager = asset_manager
        self.logger = logging.getLogger(__name__)

    def handle_organize(self, method: str = "by_category") -> Dict[str, Any]:
        """Handle asset organization"""
        return self.asset_manager.organize_assets(method)


class RefineHandler:
    """Handles asset refinement operations"""

    def __init__(self, asset_manager: AssetManager):
        self.asset_manager = asset_manager
        self.logger = logging.getLogger(__name__)

    def handle_refine(
        self, token: str, refinement_type: str, parameters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Handle asset refinement"""
        return self.asset_manager.refine_asset(token, refinement_type, parameters)


class OperationDispatcher:
    """Dispatches operations to appropriate handlers"""

    def __init__(self, asset_manager: AssetManager):
        self.asset_manager = asset_manager
        self.import_handler = ImportHandler(asset_manager)
        self.export_handler = ExportHandler(asset_manager)
        self.organize_handler = OrganizeHandler(asset_manager)
        self.refine_handler = RefineHandler(asset_manager)
        self.logger = logging.getLogger(__name__)

    def execute(self, operation: str, **kwargs) -> Dict[str, Any]:
        """
        Execute an operation by type

        Args:
            operation: Operation type (import, export, organize, refine)
            **kwargs: Operation-specific parameters
        """
        try:
            if operation == "import":
                return self.import_handler.handle_import(**kwargs)
            elif operation == "export":
                return self.export_handler.handle_export(**kwargs)
            elif operation == "organize":
                return self.organize_handler.handle_organize(**kwargs)
            elif operation == "refine":
                return self.refine_handler.handle_refine(**kwargs)
            else:
                return {"success": False, "error": f"Unknown operation: {operation}"}
        except Exception as e:
            self.logger.error(f"Error executing operation {operation}: {e}")
            return {"success": False, "error": str(e)}
