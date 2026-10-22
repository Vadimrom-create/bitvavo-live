# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-22T10:02:55.288555+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.667 | entrée 5.850 | trend 8.650 | rang 7.238
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.238
2. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.997
3. CVX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.933

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 7.898/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 6.395/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.721/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — BUILDING_ACCELERATION — score 5.393/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVX-EUR — BUILDING_ACCELERATION — score 5.359/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — BUILDING_ACCELERATION — score 5.113/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOSO-EUR — BUILDING_ACCELERATION — score 5.111/10 — DETECTED_BUT_TOO_LATE
- MASK-EUR — BUILDING_ACCELERATION — score 4.926/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 4.784/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ORCA-EUR — MEMORY_24H — score mémoire 8.261/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources ACCELERATION — WATCH_ONLY
- MOODENG-EUR — MEMORY_DECAY_24_72H — score mémoire 7.759/10 — sources ACCELERATION — MEMORY_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.670/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_DECAY_24_72H — score mémoire 7.639/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 7.606/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — MEMORY_24H — score mémoire 7.518/10 — sources ACCELERATION — MEMORY_ONLY
- W-EUR — MEMORY_DECAY_24_72H — score mémoire 7.427/10 — sources ACCELERATION — MEMORY_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 7.328/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.238/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PTB-EUR +37.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +29.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BILL-EUR +13.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DGB-EUR +12.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARKM-EUR +10.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +10.32% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AVA-EUR +9.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +9.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VVV-EUR +8.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +8.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
