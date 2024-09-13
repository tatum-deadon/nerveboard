"""CLI entry point."""

import argparse


def main():
    parser = argparse.ArgumentParser(prog="nerveboard", description="Developer Dashboard")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init", help="Initialize nerveboard")
    dash_p = sub.add_parser("dashboard", help="Show dashboard")
    dash_p.add_argument("--repo", default=".")
    sub.add_parser("report", help="Generate weekly report")

    args = parser.parse_args()

    if args.command == "dashboard":
        from nerveboard import Analytics, Dashboard
        analytics = Analytics(args.repo if hasattr(args, "repo") else ".")
        dashboard = Dashboard(analytics)
        dashboard.print()
    elif args.command == "report":
        from nerveboard import Analytics
        from nerveboard.reports import WeeklyReport
        report = WeeklyReport(Analytics("."))
        print(report.to_text())
    elif args.command is None:
        parser.print_help()
    else:
        print(f"Command '{args.command}' ready.")


if __name__ == "__main__":
    main()
