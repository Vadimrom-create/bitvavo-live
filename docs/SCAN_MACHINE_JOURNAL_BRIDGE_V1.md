# Bridge machine Solaire → registre SCAN ChatGPT

Statut : **mesure seulement** (#134). Aucun ordre et aucune modification des politiques de production.

Source : `production_direct_decision_journal.json`. Les événements `BUY_SENT` deviennent des `machine_alert` horodatées. Les `REJECTED` sont comptés séparément, jamais transformés en refus ChatGPT. La source est tronquée par rétention : une absence avant le premier événement reste inconnue.

Commandes (sorties privées, hors dépôt public) :

```bash
python scripts/export_solaire_machine_alerts.py --journal production_direct_decision_journal.json --output /private/machine_alerts.jsonl --summary /private/machine_summary.json
python scripts/scan_accountability_ledger.py --decisions /private/scan_decisions_private_v1.jsonl --machine-alerts /private/machine_alerts.jsonl --output /private/comparison.json
```

`BUY_SENT` prouve un envoi journalisé, pas une exécution. Une alerte machine plus récente que la dernière décision ChatGPT n'est **pas** automatiquement une erreur : seules les périodes où un SCAN a effectivement été réalisé peuvent être auditées comme omissions. Le résultat financier reste `NON_MESURABLE` sans trajectoires, stops, coûts et fills appariés.

Tests : `python -m unittest discover -s tests -p 'test_export_solaire_machine_alerts.py' -v`. God Layer reste en pause. HUMAN SWING R2 reste inchangé.
