# Audit Solaire #89 — livrable final

Rapport final publié : https://github.com/Vadimrom-create/bitvavo-live/issues/89#issuecomment-5860106805

Le rapport FINAL et les fichiers final_* font autorité. Les anciens fichiers metrics.json et les trades C1/C2 sans préfixe F_ sont conservés pour traçabilité : ils utilisaient le début du sender, corrigé dans les résultats définitifs avec les heures Gmail.

## Reproduire hors production

Python 3 standard uniquement, depuis le dossier racine extrait :

```sh
python3 audit-output/replay.py
python3 audit-output/evidence.py
python3 audit-output/finish_audit.py
python3 audit-output/gate_details.py
python3 audit-output/priority_replay.py
python3 audit-output/small_size_shadow.py
```

`bars.sqlite` contient les bougies avec leur première disponibilité archivée. Si absent, supprimer aussi `archive_summary.json` puis lancer replay.py pour reconstruire depuis les archives hashées. Le manifeste porte les références Git immuables. Les scripts ne passent pas d'ordre et ne modifient pas la production.

Pour régénérer le rapport : `python3 audit-output/make_report.py` puis `python3 audit-output/finalize_report.py`. La sensibilité aux bougies sans transaction est fournie comme sortie du premier replay ; sa fonction se trouve dans replay.simulate(require_trade_bar=True).

## Fichiers principaux

- Audit_Solaire_2026-09-27_FINAL.md et Tableau_10_actifs_FINAL.csv.
- final_metrics.json/csv, final_cohorts.json/csv, final_deltas.json/csv : comparaisons communes et contrôles.
- trades_F_* et dispositions_F_* : toutes les entrées, PnL, MFE/MAE, stops et refus.
- seven_gate_details.json/csv et all_seven_gate_events.csv : détail des 7 actifs (54 événements dont 2 BUY).
- revalidation_candidates.json, revalidation_pattern.csv, revalidation_summary.json : 96 snapshots, disponibilité par publication, 74 retenus par prior thesis, 22 admissibles au modèle.
- audit-input/mail_availability.json : jointure des 125 BUY aux emails, sans présumer lecture ou achat.
- audit-input/revalidation_publication_evidence.json : vérification de 86 versions du journal, pour les 96 snapshots.
- timeline_archive.csv, timeline_journals.csv et funnel_targets_extracted.json : preuves par couche. L'extrait funnel contient aussi des observations postérieures, jamais utilisées pour décider avant cutoff.

Les emails bruts et le contexte conversationnel sont des preuves privées conservées dans ce pack pour le destinataire de l'audit ; ils ne sont pas joints à l'issue publique. Les métriques sont issues d'un modèle de fill, pas de transactions réelles. Les données inconnues, notamment les bids complets, restent inconnues.

Le correctif d'ordre chronologique est appliqué au replay d'audit ; aucun correctif de production n'a été commité, déployé ou fusionné par cet audit.
