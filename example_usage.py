from client import TerminalFirstDeveloperAgentWorkspaceNavigatorClient

def main():
    client = TerminalFirstDeveloperAgentWorkspaceNavigatorClient()
    res = client.execute_terminal_goal("Check repo status and run test suite")
    print(f"Exit Code: {res['exit_code']}")
    print(f"Command Executed: {res['shell_command_executed']}")
    print(f"Feedback: {res['summary_feedback']}")

if __name__ == "__main__":
    main()
