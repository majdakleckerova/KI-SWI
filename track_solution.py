import time
import subprocess
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

solution_file = Path(sys.argv[1])
test_file = sys.argv[2]

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.start_time = None
        self.iterations = 0
        self.tracking = False

    def on_modified(self, event):
        if event.src_path.endswith(solution_file.name):
            if not self.tracking:
                print(f"Začínám měřit čas pro {solution_file.name}")
                self.start_time = time.time()
                self.tracking = True
            self.run_tests()

    def run_tests(self):
        self.iterations += 1
        print(f"[{self.iterations}] Spouštím test: {test_file}")
        test_module = test_file.replace("/", ".").removesuffix(".py")
        result = subprocess.run([sys.executable, "-m", test_module], capture_output=True, text=True)
        if result.returncode == 0:
            duration = time.time() - self.start_time
            print(f"Testy úspěšné po {self.iterations} iteracích")
            print(f"Celkový čas: {duration:.2f} sekund")
            observer.stop()
        else:
            print(result.stdout)
            print("Test selhal, čekám na další úpravu...")

if __name__ == "__main__":
    if not solution_file.exists():
        print(f"Soubor {solution_file} neexistuje.")
        sys.exit(1)

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=str(solution_file.parent), recursive=False)
    print(f"Sleduji {solution_file} pro změny... (CTRL+C pro ukončení)")
    observer.start()

    try:
        while observer.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
