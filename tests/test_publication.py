import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/publish_data.py'
spec = importlib.util.spec_from_file_location('publisher', SCRIPT)
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)


def run(*args, cwd):
    return subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True, text=True)


class PublicationTests(unittest.TestCase):
    def test_concurrent_executor_write_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            remote, scanner, writer = [root / n for n in ('remote.git', 'scanner', 'writer')]
            run('init', '--bare', '--initial-branch=main', str(remote), cwd=root)
            run('clone', str(remote), str(scanner), cwd=root)
            for path in (scanner,):
                run('config', 'user.name', 'Test', cwd=path)
                run('config', 'user.email', 'test@example.invalid', cwd=path)
            (scanner / 'pipeline_health.json').write_text('{}')
            run('add', '.', cwd=scanner); run('commit', '-m', 'seed', cwd=scanner)
            run('push', 'origin', 'main', cwd=scanner)
            run('clone', str(remote), str(writer), cwd=root)
            run('config', 'user.name', 'Test', cwd=writer)
            run('config', 'user.email', 'test@example.invalid', cwd=writer)
            (writer / 'executor_status.json').write_text('{"keep":true}')
            run('add', '.', cwd=writer); run('commit', '-m', 'executor update', cwd=writer)
            run('push', 'origin', 'main', cwd=writer)
            (scanner / 'pipeline_health.json').write_text('{"status":"OK"}')
            previous = os.getcwd()
            try:
                os.chdir(scanner)
                with patch('sys.argv', ['publish_data.py']): publisher.main()
            finally:
                os.chdir(previous)
            self.assertEqual((scanner/'executor_status.json').read_text(), '{"keep":true}')
            self.assertEqual(run('show', 'main:pipeline_health.json', cwd=remote).stdout, '{"status":"OK"}')

    def test_generated_state_conflict_stops_publication(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            remote, scanner, writer = [root / n for n in ('remote.git', 'scanner', 'writer')]
            run('init', '--bare', '--initial-branch=main', str(remote), cwd=root)
            run('clone', str(remote), str(scanner), cwd=root)
            run('config', 'user.name', 'Test', cwd=scanner)
            run('config', 'user.email', 'test@example.invalid', cwd=scanner)
            (scanner / 'pipeline_health.json').write_text('{}')
            run('add', '.', cwd=scanner); run('commit', '-m', 'seed', cwd=scanner)
            run('push', 'origin', 'main', cwd=scanner)
            run('clone', str(remote), str(writer), cwd=root)
            run('config', 'user.name', 'Test', cwd=writer)
            run('config', 'user.email', 'test@example.invalid', cwd=writer)
            (writer / 'pipeline_health.json').write_text('{"newer":true}')
            run('add', '.', cwd=writer); run('commit', '-m', 'newer scan', cwd=writer)
            run('push', 'origin', 'main', cwd=writer)
            (scanner / 'pipeline_health.json').write_text('{"status":"OK"}')
            previous = os.getcwd()
            try:
                os.chdir(scanner)
                with patch('sys.argv', ['publish_data.py']), self.assertRaises(RuntimeError): publisher.main()
            finally:
                os.chdir(previous)
            self.assertEqual(run('show', 'main:pipeline_health.json', cwd=remote).stdout, '{"newer":true}')


if __name__ == '__main__': unittest.main()
