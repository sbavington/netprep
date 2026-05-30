#!/usr/bin/env python3
import importlib.util, shutil, os, pprint, re, sys

TARGET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "network_content.py")

REMAP = {
    "1-1": "1-3",
    "1-2": "1-4",
    "1-4": "1-2",
    "3-1": "4-2",
    "3-2": "4-2",
    "3-3": "4-4",
    "4-1": "5-1",
    "4-2": "5-3",
    "5-1": "4-3",
    "5-2": "6-2",
    "5-3": "6-1",
    "5-4": "6-3",
    "5-5": "6-5",
    "6-2": "6-4",
    "8-1": "7-1",
    "8-2": "7-2",
    "8-3": "3-5",
    "8-4": "7-4",
    "8-5": "8-2",
    "8-6": "7-3",
}

spec = importlib.util.spec_from_file_location("network_content", TARGET)
mod  = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

if not hasattr(mod, "LESSON_CONTENT"):
    sys.exit("ERROR: LESSON_CONTENT dict not found in network_content.py")

old = mod.LESSON_CONTENT
new = dict(old)

for dest, src in REMAP.items():
    if src not in old:
        print(f"  WARNING: source key '{src}' not found — skipping '{dest}'")
        continue
    new[dest] = old[src]
    print(f"  {dest} <- {src}")

content_repr = pprint.pformat(new, indent=4, width=120)
new_source = f"LESSON_CONTENT = {content_repr}\n"

shutil.copy2(TARGET, TARGET + ".bak")
print(f"\nBackup written to {TARGET}.bak")

with open(TARGET, "r") as f:
    original = f.read()

match = re.search(r"^LESSON_CONTENT\s*=\s*", original, re.MULTILINE)
if match:
    prefix = original[:match.start()]
    new_file = prefix + new_source
else:
    new_file = new_source

with open(TARGET, "w") as f:
    f.write(new_file)

print(f"Done. network_content.py updated ({len(new)} keys total).")
print("\nNow restart the app:")
print("  kill -HUP \$(cat ~/app/gunicorn.ctl)")
