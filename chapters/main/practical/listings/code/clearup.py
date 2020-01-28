#   will remove target duplicates and child-parent hierarchy
def clearup_targets(self):
    final_dirs = set()
    for x in self.target_dirs:
        final_dirs.add(str(Path(x).parent))

    self.target_dirs.clear()
    self.target_dirs.extend(final_dirs)