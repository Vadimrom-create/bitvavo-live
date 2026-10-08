# Utilisation : registre privé des décisions SCAN

**Statut :** CLI d'analyse hors production, read-only ; suit l'issue #134 et le contrat `docs/SCAN_DECISION_ACCOUNTABILITY_V1.md`. Aucun ordre, aucune modification de V4 / Decision Layer / HUMAN SWING.

## Stockage réellement disponible

Un journal privé est initialisé dans la bibliothèque ChatGPT :

`/Bitvavo-Audit/scan_decisions_private_v1.jsonl`

Le fichier commence par une ligne `ledger_header` avec **0 décision SCAN historique reconstituée**. Il s'agit d'un espace *privé* distinct du dépôt **public**. La capture est **assistée dans le chat** : à chaque SCAN, ChatGPT doit ajouter une ligne de décision après avoir vérifié les preuves, en conservant l'identifiant et la version du fichier. Il n'existe **pas de hook automatique transparent** entre l'envoi d'un message ChatGPT et ce journal. Un journal absent ou non actualisé doit être signalé comme tel.

### Exemple de format (FICTIF, ne pas enregistrer comme trade réel)

```json
{"record_type":"scan_decision","decision_id":"demo-20261008-001","market":"DEMO-EUR","source_at_utc":"2026-10-08T10:00:00Z","decision_at_utc":"2026-10-08T10:02:00Z","solaire_action":"ACHETE","chatgpt_action":"WAIT_RECHECK","reason_codes":["UPCOMING_MACRO_EVENT"],"recheck_trigger":"new machine confirmation or macro event passes","recheck_due_utc":"2026-10-08T12:00:00Z","spread_pct":0.2,"book_asof_utc":"2026-10-08T10:01:00Z","roundtrip_150eur_pct":0.45}
```

Valeurs `chatgpt_action` : `BUY`, `WAIT_RECHECK`, `REJECT_STRUCTURAL`, `INSUFFICIENT_DATA`.
`solaire_action` : `ACHETE`, `WATCH`, `NONE`, `UNKNOWN`.

Un refus temporaire exige une raison, un déclencheur et une échéance. Un nouveau signal machine reçu **après** un refus doit être réévalué : ne jamais hériter d'un veto des anciens SCAN.

### Événements Solaire complémentaires (facultatif)

Exporter, avec date et identifiant immuables, les alertes Solaire historisées :
```json
{"record_type":"machine_alert","signal_id":"demo-alert-002","market":"DEMO-EUR","signal_at_utc":"2026-10-08T12:15:00Z","action":"ACHETE"}
```
En l'absence de cette source, l'outil ne peut pas détecter une confirmation postérieure ; **absence de donnée ≠ absence d'alerte**.

### Comparaison économique (optionnelle, preuve externe obligatoire)

Une ligne par décision et horizon dans un **fichier privé distinct** :
```json
{"record_type":"paired_outcome","decision_id":"demo-20261008-001","horizon_hours":4,"both_executions_validated":true,"matched_budget_policy_costs":true,"horizon_matured":true,"independent_episode":true,"solaire_net_eur":1.10,"chatgpt_net_eur":-0.25}
```

Ce format signifie que les **deux simulations appariées** ont été vérifiées séparément : fills réalistes, même capital, risque, sortie, frais et horizon. Les `true` sont des **attestations en amont**, pas des vérifications faites par l'outil. Ne jamais les saisir à partir du seul prix maximum futur ou par complaisance. Si la preuve manque, omettre le pair et publier `NON_MESURABLE`.

## Exécution locale privée

Exporter les JSONL depuis la bibliothèque dans un répertoire **hors du clone GitHub public**, puis :

```bash
python scripts/scan_accountability_ledger.py \
  --decisions /path/private/scan_decisions_private_v1.jsonl \
  --machine-alerts /path/private/solaire_alerts.jsonl \
  --pairs /path/private/paired_outcomes.jsonl \
  --asof 2026-10-09T00:00:00Z \
  --output /path/private/accountability_result.json
```

Sans `--machine-alerts` ou `--pairs`, la collecte des décisions fonctionne mais l'attribution du PnL reste **NON_MESURABLE**.

### Protections

- L'outil refuse les chemins du journal, des pairs et de la sortie **dans ce dépôt public**.
- Refuse les décisions antidatées ou dans le futur, doublons, sources plus récentes que l'arbitrage.
- Reporte les sources âgées de plus de 10 minutes et les refus sans donnée de carnet.
- Mesure le temps humain uniquement si la durée a été réellement consignée.
- N'envoie aucun email, ne passe aucun ordre et ne publie aucune transaction.

### Tests

```bash
python -m unittest discover -s tests -p 'test_scan_accountability_ledger.py' -v
```

**Limitation restante P0 :** il n'existe pas de collecte automatique des messages ChatGPT ni de moteur de replay d'exécution apparié dans cette PR. Ces travaux restent ouverts et ne doivent pas être présentés comme livrés.
