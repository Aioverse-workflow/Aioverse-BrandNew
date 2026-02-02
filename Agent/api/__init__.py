"""
Aioverse Asset Agent - API Module
REST API interface for asset management
"""

__version__ = "1.0.0"
__author__ = "Aioverse Team"
__all__ = ["run_api_server", "AssetAgentAPIHandler"]

from .rest_api import run_api_server, AssetAgentAPIHandler

# Quick start
if __name__ == "__main__":
    run_api_server()
