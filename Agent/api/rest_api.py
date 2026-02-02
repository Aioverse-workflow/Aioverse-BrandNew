"""
Aioverse Asset Agent - REST API
HTTP/REST interface for the Asset Management Agent
Built with native Python (http.server) - zero dependencies
"""

import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Tuple
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import AssetAgentAPI
from config.settings import STORAGE_CONFIG

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - REST API - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AssetAgentAPIHandler(BaseHTTPRequestHandler):
    """HTTP Request Handler for Asset Agent API"""
    
    # Class variable to share API instance
    api_instance = None
    
    def do_GET(self):
        """Handle GET requests"""
        path = urlparse(self.path).path
        query_params = parse_qs(urlparse(self.path).query)
        
        try:
            # Route GET requests
            if path == "/api/health":
                self._handle_health()
            elif path == "/api/statistics":
                self._handle_get_statistics()
            elif path == "/api/assets":
                self._handle_list_assets()
            elif path == "/api/asset":
                token = query_params.get("token", [None])[0]
                self._handle_get_asset(token)
            elif path == "/api/search":
                query = query_params.get("query", [None])[0]
                search_type = query_params.get("type", ["token"])[0]
                self._handle_search(query, search_type)
            elif path == "/api/tags":
                self._handle_get_all_tags()
            elif path == "/api/categories":
                self._handle_get_categories()
            elif path.startswith("/docs"):
                self._handle_docs_redirect()
            else:
                self._send_error(404, "Endpoint not found")
                
        except Exception as e:
            logger.error(f"Error handling GET request: {str(e)}")
            self._send_error(500, str(e))
    
    def do_POST(self):
        """Handle POST requests"""
        path = urlparse(self.path).path
        
        try:
            # Get request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length) if content_length > 0 else b'{}'
            data = json.loads(body.decode('utf-8')) if body else {}
            
            # Route POST requests
            if path == "/api/import":
                self._handle_import(data)
            elif path == "/api/export":
                self._handle_export(data)
            elif path == "/api/organize":
                self._handle_organize(data)
            elif path == "/api/refine":
                self._handle_refine(data)
            elif path == "/api/validate":
                self._handle_validate(data)
            elif path == "/api/add-tags":
                self._handle_add_tags(data)
            elif path == "/api/remove-tags":
                self._handle_remove_tags(data)
            else:
                self._send_error(404, "Endpoint not found")
                
        except json.JSONDecodeError:
            self._send_error(400, "Invalid JSON in request body")
        except Exception as e:
            logger.error(f"Error handling POST request: {str(e)}")
            self._send_error(500, str(e))
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self._add_cors_headers()
        self.end_headers()
    
    # Health Check Endpoint
    def _handle_health(self):
        """GET /api/health - Check API health"""
        response = {
            "status": "healthy",
            "service": "Aioverse Asset Agent API",
            "version": "1.0.0",
            "timestamp": str(Path(STORAGE_CONFIG["metadata_file"]).stat().st_mtime)
        }
        self._send_json_response(200, response)
    
    # Statistics Endpoint
    def _handle_get_statistics(self):
        """GET /api/statistics - Get asset statistics"""
        try:
            stats = self.api_instance.get_statistics()
            self._send_json_response(200, stats)
        except Exception as e:
            self._send_error(500, f"Failed to get statistics: {str(e)}")
    
    # List Assets Endpoint
    def _handle_list_assets(self):
        """GET /api/assets - List all assets"""
        try:
            stats = self.api_instance.get_statistics()
            metadata_file = STORAGE_CONFIG["metadata_file"]
            
            if metadata_file.exists():
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                
                assets_list = [
                    {
                        "token": token,
                        "name": meta.get("standardized_name", ""),
                        "category": meta.get("category", ""),
                        "family": meta.get("family", ""),
                        "tags": meta.get("tags", [])
                    }
                    for token, meta in metadata.items()
                ]
                
                response = {
                    "total": len(assets_list),
                    "assets": assets_list
                }
                self._send_json_response(200, response)
            else:
                self._send_json_response(200, {"total": 0, "assets": []})
                
        except Exception as e:
            self._send_error(500, f"Failed to list assets: {str(e)}")
    
    # Get Asset Endpoint
    def _handle_get_asset(self, token: str):
        """GET /api/asset?token=TOKEN - Get specific asset info"""
        if not token:
            self._send_error(400, "Token parameter required")
            return
        
        try:
            asset_info = self.api_instance.get_asset_info(token)
            self._send_json_response(200, asset_info)
        except ValueError as e:
            self._send_error(404, str(e))
        except Exception as e:
            self._send_error(500, f"Failed to get asset: {str(e)}")
    
    # Search Endpoint
    def _handle_search(self, query: str, search_type: str):
        """GET /api/search?query=Q&type=TYPE - Search assets"""
        if not query:
            self._send_error(400, "Query parameter required")
            return
        
        try:
            results = self.api_instance.search_assets(query, search_type)
            response = {
                "query": query,
                "search_type": search_type,
                "total": len(results),
                "results": results
            }
            self._send_json_response(200, response)
        except Exception as e:
            self._send_error(500, f"Search failed: {str(e)}")
    
    # Tags Endpoints
    def _handle_get_all_tags(self):
        """GET /api/tags - Get all unique tags in system"""
        try:
            metadata_file = STORAGE_CONFIG["metadata_file"]
            tags_set = set()
            
            if metadata_file.exists():
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                    for meta in metadata.values():
                        tags_set.update(meta.get("tags", []))
            
            response = {
                "total": len(tags_set),
                "tags": sorted(list(tags_set))
            }
            self._send_json_response(200, response)
        except Exception as e:
            self._send_error(500, f"Failed to get tags: {str(e)}")
    
    def _handle_add_tags(self, data: Dict[str, Any]):
        """POST /api/add-tags - Add tags to asset"""
        token = data.get("token")
        tags = data.get("tags", [])
        
        if not token or not tags:
            self._send_error(400, "Token and tags array required")
            return
        
        try:
            metadata_file = STORAGE_CONFIG["metadata_file"]
            
            if metadata_file.exists():
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                
                if token in metadata:
                    existing_tags = metadata[token].get("tags", [])
                    # Add new tags, avoid duplicates
                    for tag in tags:
                        if tag not in existing_tags:
                            existing_tags.append(tag)
                    
                    metadata[token]["tags"] = existing_tags
                    
                    with open(metadata_file, 'w') as f:
                        json.dump(metadata, f, indent=2)
                    
                    response = {
                        "token": token,
                        "tags": existing_tags,
                        "message": "Tags added successfully"
                    }
                    self._send_json_response(200, response)
                else:
                    self._send_error(404, f"Asset not found: {token}")
            else:
                self._send_error(500, "Metadata file not found")
                
        except Exception as e:
            self._send_error(500, f"Failed to add tags: {str(e)}")
    
    def _handle_remove_tags(self, data: Dict[str, Any]):
        """POST /api/remove-tags - Remove tags from asset"""
        token = data.get("token")
        tags = data.get("tags", [])
        
        if not token or not tags:
            self._send_error(400, "Token and tags array required")
            return
        
        try:
            metadata_file = STORAGE_CONFIG["metadata_file"]
            
            if metadata_file.exists():
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                
                if token in metadata:
                    existing_tags = metadata[token].get("tags", [])
                    # Remove specified tags
                    for tag in tags:
                        if tag in existing_tags:
                            existing_tags.remove(tag)
                    
                    metadata[token]["tags"] = existing_tags
                    
                    with open(metadata_file, 'w') as f:
                        json.dump(metadata, f, indent=2)
                    
                    response = {
                        "token": token,
                        "tags": existing_tags,
                        "message": "Tags removed successfully"
                    }
                    self._send_json_response(200, response)
                else:
                    self._send_error(404, f"Asset not found: {token}")
            else:
                self._send_error(500, "Metadata file not found")
                
        except Exception as e:
            self._send_error(500, f"Failed to remove tags: {str(e)}")
    
    # Categories Endpoint
    def _handle_get_categories(self):
        """GET /api/categories - Get all asset categories"""
        try:
            metadata_file = STORAGE_CONFIG["metadata_file"]
            categories_set = set()
            
            if metadata_file.exists():
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                    for meta in metadata.values():
                        cat = meta.get("category")
                        if cat:
                            categories_set.add(cat)
            
            response = {
                "total": len(categories_set),
                "categories": sorted(list(categories_set))
            }
            self._send_json_response(200, response)
        except Exception as e:
            self._send_error(500, f"Failed to get categories: {str(e)}")
    
    # Import Endpoint
    def _handle_import(self, data: Dict[str, Any]):
        """POST /api/import - Import asset"""
        file_path = data.get("file_path")
        metadata = data.get("metadata", {})
        
        if not file_path:
            self._send_error(400, "file_path required")
            return
        
        try:
            result = self.api_instance.import_asset(file_path, metadata)
            self._send_json_response(201, result)
        except Exception as e:
            self._send_error(400, f"Import failed: {str(e)}")
    
    # Export Endpoint
    def _handle_export(self, data: Dict[str, Any]):
        """POST /api/export - Export asset"""
        token = data.get("token")
        export_path = data.get("export_path")
        
        if not token or not export_path:
            self._send_error(400, "token and export_path required")
            return
        
        try:
            result = self.api_instance.export_asset(token, export_path)
            self._send_json_response(200, result)
        except Exception as e:
            self._send_error(400, f"Export failed: {str(e)}")
    
    # Organize Endpoint
    def _handle_organize(self, data: Dict[str, Any]):
        """POST /api/organize - Organize assets"""
        method = data.get("method", "category")
        
        try:
            result = self.api_instance.organize_assets(method)
            response = {
                "method": method,
                "organization": result,
                "message": "Assets organized successfully"
            }
            self._send_json_response(200, response)
        except Exception as e:
            self._send_error(400, f"Organization failed: {str(e)}")
    
    # Refine Endpoint
    def _handle_refine(self, data: Dict[str, Any]):
        """POST /api/refine - Refine asset"""
        token = data.get("token")
        refinements = data.get("refinements", {})
        
        if not token:
            self._send_error(400, "token required")
            return
        
        try:
            result = self.api_instance.refine_asset(token, refinements)
            self._send_json_response(200, result)
        except Exception as e:
            self._send_error(400, f"Refinement failed: {str(e)}")
    
    # Validate Endpoint
    def _handle_validate(self, data: Dict[str, Any]):
        """POST /api/validate - Validate asset"""
        token = data.get("token")
        
        if not token:
            self._send_error(400, "token required")
            return
        
        try:
            result = self.api_instance.validate_asset(token)
            self._send_json_response(200, result)
        except Exception as e:
            self._send_error(400, f"Validation failed: {str(e)}")
    
    # Docs Endpoint
    def _handle_docs_redirect(self):
        """Redirect /docs to API documentation"""
        self.send_response(301)
        self.send_header('Location', '/docs/API_DOCUMENTATION.md')
        self.end_headers()
    
    # Helper Methods
    def _send_json_response(self, status_code: int, data: Dict[str, Any]):
        """Send JSON response"""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self._add_cors_headers()
        self.end_headers()
        
        response = json.dumps(data, indent=2)
        self.wfile.write(response.encode('utf-8'))
        
        logger.info(f"Response: {status_code} - {data.get('message', 'OK')}")
    
    def _send_error(self, status_code: int, message: str):
        """Send error response"""
        error_response = {
            "error": True,
            "status": status_code,
            "message": message
        }
        self._send_json_response(status_code, error_response)
    
    def _add_cors_headers(self):
        """Add CORS headers for cross-origin requests"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    
    def log_message(self, format, *args):
        """Override to use our logger"""
        logger.info(format % args)


def run_api_server(host: str = 'localhost', port: int = 8000):
    """
    Start the REST API server
    
    Args:
        host: Server host (default: localhost)
        port: Server port (default: 8000)
    """
    # Initialize API instance
    AssetAgentAPIHandler.api_instance = AssetAgentAPI()
    
    # Create server
    server_address = (host, port)
    httpd = HTTPServer(server_address, AssetAgentAPIHandler)
    
    logger.info(f"🚀 Aioverse Asset Agent API Server Started")
    logger.info(f"📍 Host: {host}:{port}")
    logger.info(f"📚 API Docs: http://{host}:{port}/docs")
    logger.info(f"💚 Health: http://{host}:{port}/api/health")
    logger.info(f"🛑 Press Ctrl+C to stop")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("🛑 API Server stopped by user")
        httpd.server_close()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Aioverse Asset Agent API Server')
    parser.add_argument('--host', default='localhost', help='Host to bind to')
    parser.add_argument('--port', type=int, default=8000, help='Port to bind to')
    
    args = parser.parse_args()
    
    run_api_server(args.host, args.port)
