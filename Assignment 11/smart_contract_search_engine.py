import argparse
import os
import re


IGNORED_DIRS = {"node_modules", "artifacts", "cache", ".git", "build", "dist", "venv", ".venv"}


def collect_solidity_files(root_dir):
    results = []
    for base, _, files in os.walk(root_dir):
        parts = set(base.split(os.sep))
        if parts & IGNORED_DIRS:
            continue
        for filename in files:
            if filename.endswith(".sol"):
                results.append(os.path.join(base, filename))
    return results


def search_file(file_path, query, use_regex=False, case_sensitive=False):
    flags = 0 if case_sensitive else re.IGNORECASE
    matches = []

    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        lines = file.readlines()

    if use_regex:
        pattern = re.compile(query, flags)
        for i, line in enumerate(lines, start=1):
            if pattern.search(line):
                matches.append((i, line.rstrip()))
    else:
        needle = query if case_sensitive else query.lower()
        for i, line in enumerate(lines, start=1):
            source = line if case_sensitive else line.lower()
            if needle in source:
                matches.append((i, line.rstrip()))

    return matches


def score_result(path, matches):
    score = len(matches)
    filename = os.path.basename(path).lower()
    if "token" in filename:
        score += 1
    if "erc" in filename:
        score += 1
    return score


def run_search(root_dir, query, use_regex=False, case_sensitive=False, top_k=10):
    files = collect_solidity_files(root_dir)
    results = []

    for path in files:
        found = search_file(path, query, use_regex=use_regex, case_sensitive=case_sensitive)
        if found:
            results.append(
                {
                    "path": path,
                    "matches": found,
                    "score": score_result(path, found),
                }
            )

    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:top_k]


def main():
    parser = argparse.ArgumentParser(description="Assignment 11: Smart Contract Search Engine")
    parser.add_argument("query", help="Text or regex pattern to search in Solidity files")
    parser.add_argument("--root", default="..", help="Root directory to crawl (default: parent folder)")
    parser.add_argument("--regex", action="store_true", help="Use regex search")
    parser.add_argument("--case", action="store_true", help="Case-sensitive search")
    parser.add_argument("--top", type=int, default=10, help="Max result files to show")
    args = parser.parse_args()

    results = run_search(
        root_dir=args.root,
        query=args.query,
        use_regex=args.regex,
        case_sensitive=args.case,
        top_k=args.top,
    )

    print("Assignment 11: Smart Contract Search Engine")
    print(f"Root: {os.path.abspath(args.root)}")
    print(f"Query: {args.query}")

    if not results:
        print("\nNo matching Solidity files found.")
        return

    print(f"\nFound {len(results)} matching file(s):")
    for index, item in enumerate(results, start=1):
        print(f"\n{index}. {item['path']} (score={item['score']})")
        for line_no, snippet in item["matches"][:5]:
            print(f"   L{line_no}: {snippet}")
        if len(item["matches"]) > 5:
            print(f"   ... {len(item['matches']) - 5} more match(es)")


if __name__ == "__main__":
    main()
