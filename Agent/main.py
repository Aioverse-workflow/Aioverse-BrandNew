"""
Main entry point for the Aioverse Asset Management Agent
Provides high-level interface for asset operations
"""

import logging
from pathlib import Path

from config import AGENT_CONFIG, LOG_CONFIG
from core import AIAssetAgent, AssetManager
from handlers import OperationDispatcher
from utils import ComplianceChecker, TokenGenerator

# Configure logging
logging.basicConfig(
    level=LOG_CONFIG["level"],
    format=LOG_CONFIG["format"],
    handlers=[
        logging.FileHandler(LOG_CONFIG["file"]),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


class AssetAgentAPI:
    """
    High-level API for interacting with the Aioverse Asset Agent
    Combines AI agent capabilities with operation handlers
    """

    def __init__(self):
        """Initialize the Asset Agent API"""
        self.ai_agent = AIAssetAgent()
        self.asset_manager = self.ai_agent.asset_manager
        self.dispatcher = OperationDispatcher(self.asset_manager)
        logger.info("Asset Agent API initialized")

    def import_asset(
        self, file_path: str, token: str, category: str, family: str, variant: str, **metadata
    ) -> dict:
        """Import a new asset"""
        return self.dispatcher.execute(
            "import",
            file_path=file_path,
            token=token,
            category=category,
            family=family,
            variant=variant,
            metadata=metadata,
        )

    def export_asset(self, token: str, export_path: str, **options) -> dict:
        """Export an asset"""
        return self.dispatcher.execute(
            "export", token=token, export_path=export_path, **options
        )

    def organize_assets(self, method: str = "by_category") -> dict:
        """Organize assets"""
        return self.dispatcher.execute("organize", method=method)

    def refine_asset(self, token: str, refinement_type: str, **parameters) -> dict:
        """Refine an asset"""
        return self.dispatcher.execute(
            "refine",
            token=token,
            refinement_type=refinement_type,
            parameters=parameters,
        )

    def validate_asset(self, token: str) -> dict:
        """Validate an asset"""
        return self.asset_manager.validate_asset(token)

    def check_compliance(self, token: str) -> dict:
        """Check asset compliance"""
        try:
            metadata = self.asset_manager.get_asset_info(token)["metadata"]
            return ComplianceChecker.check_compliance(metadata)
        except Exception as e:
            return {"error": str(e)}

    def search_assets(self, query: str, search_type: str = "token") -> list:
        """Search for assets"""
        return self.asset_manager.search_assets(query, search_type)

    def get_asset_info(self, token: str) -> dict:
        """Get asset information"""
        return self.asset_manager.get_asset_info(token)

    def get_statistics(self) -> dict:
        """Get collection statistics"""
        return self.asset_manager.get_statistics()

    def process_command(self, command: str) -> dict:
        """Process natural language command through AI agent"""
        return self.ai_agent.process_command(command)

    def get_available_tools(self) -> list:
        """Get list of available tools"""
        return self.ai_agent.get_available_tools()

    def get_conversation_history(self) -> list:
        """Get AI agent conversation history"""
        return self.ai_agent.get_conversation_history()


def main():
    """Main entry point for command-line usage"""
    import sys

    api = AssetAgentAPI()

    print(f"✓ {AGENT_CONFIG['name']} v{AGENT_CONFIG['version']}")
    print(f"✓ Ready for operations\n")

    while True:
        try:
            command = input("Agent> ").strip()

            if not command:
                continue

            if command.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if command.lower() == "help":
                print("\nAvailable commands:")
                for tool in api.get_available_tools():
                    print(f"  - {tool['name']}: {tool['description']}")
                print("\nOr type any natural language command!\n")
                continue

            if command.lower() == "stats":
                stats = api.get_statistics()
                print(f"\nAsset Statistics:")
                print(f"  Total Assets: {stats.get('total_assets', 0)}")
                print(f"  Total Size: {stats.get('total_size_mb', 0)} MB")
                print(f"  By Category: {stats.get('by_category', {})}\n")
                continue

            # Process command through AI agent
            result = api.process_command(command)
            print(f"\nResult: {result}\n")

        except KeyboardInterrupt:
            print("\n\nInterrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")
            logger.exception("Command processing error")


if __name__ == "__main__":
    main()
