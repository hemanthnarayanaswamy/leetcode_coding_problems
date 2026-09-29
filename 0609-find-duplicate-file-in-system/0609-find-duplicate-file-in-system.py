class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)

        for path in paths:
            parts = path.split(" ")
            directory = parts[0]

            for file in parts[1:]:
                file_name, content = file.split("(")
                content = content[:-1]  # Remove closing ")"

                tracker[content].append(directory + "/" + file_name)

        duplicates = []

        for file_paths in tracker.values():
            if len(file_paths) > 1:
                duplicates.append(file_paths)

        return duplicates

        