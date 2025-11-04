import json
import threading
from pathlib import Path

class JSONDB:
    def __init__(self, path):
        self.path = Path(path)
        self.lock = threading.Lock()
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._write({"users": [], "cars": []})

    def _read(self):
        with self.lock:
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return {"users": [], "cars": []}

    def _write(self, obj):
        with self.lock:
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(obj, f, indent=2, ensure_ascii=False)

    def get_all(self):
        return self._read()

    def get_list(self, key):
        data = self._read()
        return data.get(key, [])

    def replace_list(self, key, new_list):
        data = self._read()
        data[key] = new_list
        self._write(data)

    def append_to_list(self, key, item):
        data = self._read()
        lst = data.get(key, [])
        lst.append(item)
        data[key] = lst
        self._write(data)
