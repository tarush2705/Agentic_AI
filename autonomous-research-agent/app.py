from agent import create_agent
from report_generator import generate_report

def run(topic):
    agent = create_agent()

    print("\n🔍 Researching...\n")
    research_data = agent.run(topic)

    print("\n📝 Generating Report...\n")
    report_prompt = generate_report(topic, research_data)

    final_report = agent.run(report_prompt)

    print("\n📄 FINAL REPORT:\n")
    print(final_report)

if __name__ == "__main__":
    topic = input("Enter Research Topic: ")
    run(topic)