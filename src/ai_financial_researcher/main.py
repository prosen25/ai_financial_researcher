#!/usr/bin/env python
import os
from ai_financial_researcher.crew import ResearchCrew

# Create a directory if it doesn't exists
os.makedirs(name="output", exist_ok=True)

def run():
    """
    Run the crew.
    """
    inputs = {"company": "Apple"}

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== Final Report ====\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()