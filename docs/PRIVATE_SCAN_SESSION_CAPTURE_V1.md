# Capture explicite des décisions SCAN dans la Library privée — V1

## Ce qui est réellement possible
La bibliothèque ChatGPT contient déjà le fichier **privé** `/Bitvavo-Audit/scan_decisions_private_v1.jsonl`, initialisé avec `ledger_header` mais sans aucune décision historique. Il n'existe **aucun hook automatique** garantissant l'accès aux messages passés ou futurs de ChatGPT. On doit donc matérialiser le fichier Library à chaque SCAN, écrire une session **pendant ce tour**, puis sauvegarder la nouvelle version dans la Library avec contrôle de version. Une simple PR GitHub ne capture pas le chat.

La nouvelle commande `scripts/capture_chatgpt_scan_session.py` réalise la **partie locale** de cette opération sans exposer les recommandations dans le dépôt public. Elle doit être exécutée avec le journal matérialisé **hors du dépôt public**.

## Contrat de réponse / conservation lors d'un vrai SCAN

1. Rassembler la source machine et sa fraîcheur, les alertes / mémoire 72 h / refus, les facteurs macro-news et la liquidité récente. Ne pas masquer les données manquantes.
2. Construire une **réponse explicite** : achat conditionné à la qualité d'exécution, attente avec déclencheur et échéance, refus structurel motivé, ou données insuffisantes. Chaque candidat réellement décidé correspond à une entrée `scan_decision`.
3. Une fois la réponse utilisateur rédigée, préserver exactement ce texte dans `assistant_final_text`, ainsi que sa fenêtre temporelle et la référence machine (commit GitHub, fichier et timestamp). **Aucun horodatage fictif** : si l'instant d'une ancienne décision est inconnu, elle reste non journalisée.
4. Matérialiser le journal privé de la Library puis ajouter la session avec la commande ci-dessous. Sauvegarder la version produite sur la **même ressource Library** ; relire et contrôler que la session est effectivement conservée. Signaler l'échec d'écriture. Éviter toute copie publique.
5. Le prochain audit comparer les alertes machine à ces décisions, puis les PnL nets des exécutions vérifiées. Tant qu'aucune décision exploitable n'est inscrite, valeur ajoutée ChatGPT = `NON_MESURABLE`.

## Format de la session d'entrée (EXEMPLE FICTIF À NE PAS COPIER COMME PREUVE)

```json
{
  "schema": "chatgpt_scan_session_capture_v1",
  "scan_id": "SCAN-20261008-EXAMPLE001",
  "session_started_at_utc": "2026-10-08T20:00:00Z",
  "session_completed_at_utc": "2026-10-08T20:05:00Z",
  "assistant_final_text": "SCAN DEMONSTRATION : attendre un nouveau signal après l'événement macro.",
  "session_status": "SCAN_WAIT",
  "machine_source_status": "FRESH",
  "machine_source_ref": "github-commit-or-blob-SHA",
  "machine_data_asof_utc": "2026-10-08T20:02:00Z",
  "reviewed_signal_ids": ["test-signal-001"],
  "decisions": [
    {
      "record_type": "scan_decision",
      "decision_id": "test-decision-001",
      "market": "OGN-EUR",
      "source_at_utc": "2026-10-08T20:02:00Z",
      "decision_at_utc": "2026-10-08T20:04:00Z",
      "solaire_action": "ACHETE",
      "chatgpt_action": "WAIT_RECHECK",
      "reason_codes": ["MACRO_PENDING"],
      "recheck_trigger": "new machine confirmation or macro event completed",
      "recheck_due_utc": "2026-10-08T21:00:00Z",
      "spread_pct": null,
      "book_asof_utc": null,
      "roundtrip_150eur_pct": null
    }
  ]
}
```

Note : l'exemple décrit volontairement une donnée de carnet manquante et ne saurait être confondu avec un achat vérifié. Une session sans décision est autorisée uniquement avec `no_decision_reason` documenté.

## Utilisation locale

```bash
python scripts/capture_chatgpt_scan_session.py \
    --session /chemin-prive/session_scan_exacte.json \
    --ledger /chemin-prive/scan_decisions_private_v1.jsonl

python scripts/scan_accountability_ledger.py \
    --decisions /chemin-prive/scan_decisions_private_v1.jsonl \
    --asof 2026-10-08T22:30:00Z
```

L'outil écrit la session et ses décisions de façon **atomique et idempotente au niveau d'un système de fichiers local**. Il ne réécrit pas l'historique existant, refuse les doublons et les dates futures, et conserve un SHA-256 du texte exact. Le lecteur de PnL existant ignore les enveloppes `scan_session` mais comptabilise les `scan_decision`.

**Attention :** la synchronisation finale dans la Library est une **seconde opération**, pas une transaction atomique globale. Utiliser le `library_file_id` et `expected_current_version` de Files, ne jamais écraser une modification concurrente sans relecture. Un succès en local sans succès de synchronisation Library ne vaut **PAS** preuve d'archivage pérenne.

## Périmètre et limites

- Un texte exact archivé n'authentifie pas à lui seul une interface ChatGPT ; c'est une preuve de ce que l'assistant a rédigé et déclaré avoir recommandé, pas une attestation indépendante de lecture/exécution.
- Une session est une interaction active ; une alerte reçue hors SCAN n'est pas automatiquement une erreur ChatGPT.
- Aucune opération réelle ou portefeuille n'est publié sur GitHub public.
- God Layer en pause ; HUMAN SWING et stratégie de production inchangés.
- Premières données financieres à mesurer **uniquement après des SCAN effectivement enregistrés** et des simulations d'exécution appariées.
