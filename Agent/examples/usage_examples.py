"""
Example usage of the Aioverse Asset Management Agent
Demonstrates all major operations
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from main import AssetAgentAPI


def example_1_basic_operations():
    """Example 1: Basic asset operations"""
    print("=" * 60)
    print("EXAMPLE 1: Basic Asset Operations")
    print("=" * 60)

    api = AssetAgentAPI()

    # Example: Process natural language commands
    commands = [
        "Show me all assets organized by category",
        "Search for LOGO assets",
        "Get statistics on our asset collection",
    ]

    for command in commands:
        print(f"\n📝 Command: {command}")
        result = api.process_command(command)
        print(f"✓ Result: {result}\n")


def example_2_asset_validation():
    """Example 2: Validate and check compliance"""
    print("=" * 60)
    print("EXAMPLE 2: Asset Validation & Compliance")
    print("=" * 60)

    api = AssetAgentAPI()

    # Example token
    token = "LOGO-AIOTIZE-PFP001"

    print(f"\n🔍 Checking token format: {token}")
    from utils import TokenGenerator

    valid, error = TokenGenerator.validate_token(token)
    if valid:
        print(f"✓ Valid token format")
        parsed = TokenGenerator.parse_token(token)
        print(f"  Components: {parsed}")
    else:
        print(f"✗ Invalid: {error}")


def example_3_direct_api_usage():
    """Example 3: Direct API usage for operations"""
    print("=" * 60)
    print("EXAMPLE 3: Direct API Usage")
    print("=" * 60)

    api = AssetAgentAPI()

    print("\n1. Get Collection Statistics")
    stats = api.get_statistics()
    print(f"   Total Assets: {stats.get('total_assets', 0)}")
    print(f"   Total Size: {stats.get('total_size_mb', 0)} MB")
    print(f"   Categories: {stats.get('by_category', {})}")

    print("\n2. Search Assets")
    results = api.search_assets("LOGO", search_type="category")
    print(f"   Found {len(results)} LOGO assets")

    print("\n3. Available Tools")
    tools = api.get_available_tools()
    print(f"   Agent has {len(tools)} tools available")
    for tool in tools[:3]:
        print(f"     - {tool['name']}: {tool['description']}")


def example_4_workflow_scenario():
    """Example 4: Complete workflow scenario"""
    print("=" * 60)
    print("EXAMPLE 4: Complete Workflow Scenario")
    print("=" * 60)

    api = AssetAgentAPI()

    print("\n📋 Workflow: Asset Management Pipeline")
    print("-" * 60)

    # Step 1: Get statistics
    print("\nStep 1: Assess current assets")
    stats = api.get_statistics()
    print(f"  Current collection size: {stats.get('total_size_mb', 0)} MB")

    # Step 2: Organize assets
    print("\nStep 2: Organize assets by category")
    result = api.organize_assets("by_category")
    print(f"  Organized {result.get('total_assets', 0)} assets")

    # Step 3: Search specific assets
    print("\nStep 3: Find logo assets")
    logos = api.search_assets("LOGO", search_type="category")
    print(f"  Found {len(logos)} logo assets")

    # Step 4: Show available tools
    print("\nStep 4: Available operations")
    tools = api.get_available_tools()
    for i, tool in enumerate(tools[:5], 1):
        print(f"  {i}. {tool['name']}")


def example_5_interactive_mode():
    """Example 5: Interactive agent mode"""
    print("=" * 60)
    print("EXAMPLE 5: Interactive AI Agent Mode")
    print("=" * 60)

    api = AssetAgentAPI()

    example_commands = [
        "What assets do we have?",
        "Organize all assets by family",
        "Show me statistics",
    ]

    print("\n📢 Sample Agent Interactions:")
    print("-" * 60)

    for i, command in enumerate(example_commands, 1):
        print(f"\n{i}. User: '{command}'")
        result = api.process_command(command)
        if isinstance(result, dict):
            if result.get("success"):
                print(f"   Agent: ✓ Operation completed successfully")
            else:
                print(f"   Agent: {result.get('message', result.get('error', 'Processing'))}")
        else:
            print(f"   Agent: {result}")


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("🚀 AIOVERSE ASSET MANAGEMENT AGENT - EXAMPLES")
    print("=" * 60)

    examples = [
        ("Basic Operations", example_1_basic_operations),
        ("Validation & Compliance", example_2_asset_validation),
        ("Direct API Usage", example_3_direct_api_usage),
        ("Workflow Scenario", example_4_workflow_scenario),
        ("Interactive Mode", example_5_interactive_mode),
    ]

    print("\nAvailable Examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")

    print("\nRunning all examples...\n")

    for name, example_func in examples:
        try:
            example_func()
            print("\n")
        except Exception as e:
            print(f"\n❌ Error in {name}: {e}\n")


if __name__ == "__main__":
    main()
