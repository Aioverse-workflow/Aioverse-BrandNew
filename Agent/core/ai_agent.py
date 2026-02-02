"""
AI Asset Agent - Intelligent asset management powered by LLM
Uses an agentic approach to handle asset operations
"""

import json
import logging
from typing import Any, Callable, Dict, List, Optional

from ..core import AssetManager


class AIAssetAgent:
    """
    AI-powered agent for managing Aioverse assets
    Uses an LLM-based approach with defined tools for asset operations
    """

    def __init__(self):
        """Initialize the AI Asset Agent"""
        self.logger = logging.getLogger(__name__)
        self.asset_manager = AssetManager()
        self.tools = self._initialize_tools()
        self.conversation_history: List[Dict[str, str]] = []

    def _initialize_tools(self) -> Dict[str, Callable]:
        """Initialize available tools for the agent"""
        return {
            "import_asset": self.asset_manager.import_asset,
            "export_asset": self.asset_manager.export_asset,
            "organize_assets": self.asset_manager.organize_assets,
            "refine_asset": self.asset_manager.refine_asset,
            "validate_asset": self.asset_manager.validate_asset,
            "search_assets": self.asset_manager.search_assets,
            "get_asset_info": self.asset_manager.get_asset_info,
            "get_statistics": self.asset_manager.get_statistics,
        }

    def process_command(self, user_input: str) -> Dict[str, Any]:
        """
        Process a user command and route to appropriate asset operation

        Args:
            user_input: User's natural language command

        Returns:
            Dictionary containing the operation result
        """
        self.logger.info(f"Processing command: {user_input}")
        self.conversation_history.append({"role": "user", "content": user_input})

        # Analyze command intent
        intent = self._analyze_intent(user_input)

        # Execute appropriate operation
        result = self._execute_operation(intent, user_input)

        # Store in conversation history
        self.conversation_history.append({"role": "assistant", "content": str(result)})

        return result

    def _analyze_intent(self, user_input: str) -> str:
        """Analyze user input to determine intent"""
        user_lower = user_input.lower()

        intent_keywords = {
            "import": ["import", "add", "register", "upload"],
            "export": ["export", "download", "extract", "save"],
            "organize": ["organize", "organize", "categorize", "sort", "group"],
            "refine": ["refine", "enhance", "optimize", "improve", "compress"],
            "validate": ["validate", "check", "verify", "audit", "compliance"],
            "search": ["search", "find", "look for", "query"],
            "info": ["info", "detail", "metadata", "status"],
            "statistics": ["stat", "report", "summary", "count"],
        }

        for intent, keywords in intent_keywords.items():
            if any(keyword in user_lower for keyword in keywords):
                return intent

        return "unknown"

    def _execute_operation(self, intent: str, user_input: str) -> Dict[str, Any]:
        """Execute operation based on detected intent"""
        try:
            if intent == "import":
                return self._handle_import(user_input)
            elif intent == "export":
                return self._handle_export(user_input)
            elif intent == "organize":
                return self._handle_organize(user_input)
            elif intent == "refine":
                return self._handle_refine(user_input)
            elif intent == "validate":
                return self._handle_validate(user_input)
            elif intent == "search":
                return self._handle_search(user_input)
            elif intent == "info":
                return self._handle_info(user_input)
            elif intent == "statistics":
                return self._handle_statistics(user_input)
            else:
                return {
                    "success": False,
                    "error": "Could not determine operation from input",
                    "suggestion": "Try commands like: import asset, export asset, organize, refine, validate, search, info, or statistics",
                }
        except Exception as e:
            self.logger.error(f"Error executing operation: {e}")
            return {"success": False, "error": str(e)}

    def _handle_import(self, user_input: str) -> Dict[str, Any]:
        """Handle asset import operation"""
        # Example: "Import asset from path/to/file.png as LOGO-AIOTIZE-PFP001 in logos category"
        return {
            "operation": "import",
            "status": "pending",
            "message": "Import operation requires file path and token details. Please provide: file_path, token, category, family, variant",
            "example": "asset_manager.import_asset('/path/to/file.png', 'LOGO-AIOTIZE-PFP001', 'LOGO', 'AIOTIZE', 'PFP')",
        }

    def _handle_export(self, user_input: str) -> Dict[str, Any]:
        """Handle asset export operation"""
        return {
            "operation": "export",
            "status": "pending",
            "message": "Export operation requires asset token and destination path. Please provide: token, export_path",
            "example": "asset_manager.export_asset('LOGO-AIOTIZE-PFP001', './exports')",
        }

    def _handle_organize(self, user_input: str) -> Dict[str, Any]:
        """Handle asset organization"""
        method = "by_category"
        if "family" in user_input.lower():
            method = "by_family"
        elif "status" in user_input.lower():
            method = "by_status"

        return self.asset_manager.organize_assets(method)

    def _handle_refine(self, user_input: str) -> Dict[str, Any]:
        """Handle asset refinement"""
        return {
            "operation": "refine",
            "status": "pending",
            "message": "Refine operation requires token, refinement type, and parameters. Options: compress, optimize, convert, enhance",
            "example": "asset_manager.refine_asset('LOGO-AIOTIZE-PFP001', 'optimize', {'quality': 95})",
        }

    def _handle_validate(self, user_input: str) -> Dict[str, Any]:
        """Handle asset validation"""
        # Extract token from input if possible
        tokens = self._extract_tokens(user_input)
        if tokens:
            return self.asset_manager.validate_asset(tokens[0])
        return {
            "operation": "validate",
            "status": "pending",
            "message": "Validation requires asset token. Please specify which asset to validate.",
        }

    def _handle_search(self, user_input: str) -> Dict[str, Any]:
        """Handle asset search"""
        # Extract search query
        keywords = user_input.lower().split()
        search_query = " ".join([kw for kw in keywords if kw not in ["search", "find", "look", "for", "by"]])

        if search_query:
            return {
                "operation": "search",
                "results": self.asset_manager.search_assets(search_query),
                "query": search_query,
            }
        return {"operation": "search", "status": "pending", "message": "Please specify what to search for"}

    def _handle_info(self, user_input: str) -> Dict[str, Any]:
        """Handle asset info retrieval"""
        tokens = self._extract_tokens(user_input)
        if tokens:
            return self.asset_manager.get_asset_info(tokens[0])
        return {
            "operation": "info",
            "status": "pending",
            "message": "Please specify asset token",
        }

    def _handle_statistics(self, user_input: str) -> Dict[str, Any]:
        """Handle statistics request"""
        return self.asset_manager.get_statistics()

    def _extract_tokens(self, text: str) -> List[str]:
        """Extract asset tokens from text (format: PREFIX-FAMILY-VARIANT###)"""
        import re

        pattern = r"\b[A-Z]{3,}-[A-Z]+-[A-Z]+\d{3,}\b"
        return re.findall(pattern, text.upper())

    def get_available_tools(self) -> List[Dict[str, Any]]:
        """Return list of available tools for the agent"""
        return [
            {
                "name": "import_asset",
                "description": "Import and register a new asset in the Aioverse system",
                "parameters": {
                    "file_path": "Path to the asset file",
                    "token": "Unique token (e.g., LOGO-AIOTIZE-PFP001)",
                    "category": "Asset category (LOGO, ICON, etc.)",
                    "family": "Asset family (AIOTIZE, AIOVERSE, etc.)",
                    "variant": "Asset variant (PFP, MARK, etc.)",
                },
            },
            {
                "name": "export_asset",
                "description": "Export an asset with metadata",
                "parameters": {
                    "token": "Asset token to export",
                    "export_path": "Destination path for export",
                    "include_metadata": "Include metadata JSON file",
                },
            },
            {
                "name": "organize_assets",
                "description": "Organize assets by category, family, or status",
                "parameters": {"organization_method": "by_category | by_family | by_status"},
            },
            {
                "name": "refine_asset",
                "description": "Apply refinements to an asset (compress, optimize, etc.)",
                "parameters": {
                    "token": "Asset token",
                    "refinement_type": "compress | optimize | convert | enhance",
                    "parameters": "Refinement-specific parameters",
                },
            },
            {
                "name": "validate_asset",
                "description": "Validate asset compliance with Aioverse standards",
                "parameters": {"token": "Asset token to validate"},
            },
            {
                "name": "search_assets",
                "description": "Search assets by token, name, category, or tag",
                "parameters": {
                    "query": "Search query",
                    "search_type": "token | name | category | tag",
                },
            },
            {
                "name": "get_statistics",
                "description": "Get overall statistics about the asset collection",
                "parameters": {},
            },
        ]

    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get the conversation history"""
        return self.conversation_history

    def clear_conversation_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
