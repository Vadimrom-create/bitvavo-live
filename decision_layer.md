# Decision Layer V1 — shadow

Scan : 2026-09-10T15:06:47.939683+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : KAS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.409 | entrée 6.000 | trend 8.550 | rang 7.446
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 8.007 | entrée 5.050 | trend 9.200 | rang 5.503
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.339 | entrée 5.950 | trend 8.650 | rang 7.489
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.489
2. KAS-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.446
3. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.351

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
