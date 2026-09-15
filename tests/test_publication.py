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
    def test_current_data_load_does_not_replace_code_or_revision(self):
        from scripts.load_public_state import load
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);code=root/'code';data=root/'data';code.mkdir();data.mkdir()
            for p in (code,data):
                run('init','--initial-branch=main',cwd=p)
                run('config','user.name','Test',cwd=p);run('config','user.email','test@example.invalid',cwd=p)
                (p/'pipeline.py').write_text('validated' if p==code else 'unreviewed')
                (p/'v4_history.json').write_text('{}' if p==code else '{"latest":true}')
                run('add','.',cwd=p);run('commit','-m','seed',cwd=p)
            before=run('rev-parse','HEAD',cwd=code).stdout
            load(data,code)
            self.assertEqual((code/'pipeline.py').read_text(),'validated')
            self.assertEqual((code/'v4_history.json').read_text(),'{"latest":true}')
            self.assertEqual(run('rev-parse','HEAD',cwd=code).stdout,before)

    def test_single_historical_file_divergence_is_refused_before_push(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            run('init','--initial-branch=main',cwd=root)
            run('config','user.name','Test',cwd=root);run('config','user.email','test@example.invalid',cwd=root)
            p=root/'history_corrected/2026-09-11/s1.json.gz';p.parent.mkdir(parents=True);p.write_bytes(b'original')
            run('add','.',cwd=root);run('commit','-m','seed',cwd=root)
            p.write_bytes(b'changed')
            with self.assertRaisesRegex(RuntimeError,'IMMUTABLE_JOURNAL_CONFLICT'):
                publisher.publish([str(p.relative_to(root))],'must fail',source=root)

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
            source_head = run('rev-parse', 'HEAD', cwd=scanner).stdout
            previous = os.getcwd()
            try:
                os.chdir(scanner)
                publisher.publish(publisher.GENERATED,'test publication')
            finally:
                os.chdir(previous)
            self.assertFalse((scanner/'executor_status.json').exists())
            self.assertEqual(run('rev-parse', 'HEAD', cwd=scanner).stdout, source_head)
            self.assertEqual(run('show', 'main:executor_status.json', cwd=remote).stdout, '{"keep":true}')
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
            source_head = run('rev-parse', 'HEAD', cwd=scanner).stdout
            previous = os.getcwd()
            try:
                os.chdir(scanner)
                with self.assertRaises(RuntimeError): publisher.publish(publisher.GENERATED,'test conflict')
            finally:
                os.chdir(previous)
            self.assertEqual(run('show', 'main:pipeline_health.json', cwd=remote).stdout, '{"newer":true}')


if __name__ == '__main__': unittest.main()
