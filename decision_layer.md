# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-22T00:14:22.178707+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.197 | entrée 7.250 | trend 8.450 | rang 7.625
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : KMNO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.590 | entrée 6.200 | trend 7.750 | rang 7.027
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : METIS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.808 | entrée 6.450 | trend 8.200 | rang 7.328
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.625 — opportunité 8.197 — entrée 7.250 — trend 8.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.625
2. METIS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.328
3. CTR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.144

## Accélération indépendante

- ORCA-EUR — CONFIRMED_ACCELERATION — score 8.261/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 6.059/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 5.834/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROM-EUR — BUILDING_ACCELERATION — score 5.820/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — BUILDING_ACCELERATION — score 5.774/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 5.529/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BILL-EUR — BUILDING_ACCELERATION — score 5.392/10 — DETECTED_BUT_TOO_LATE
- DYM-EUR — BUILDING_ACCELERATION — score 5.243/10 — DETECTED_BUT_TOO_LATE
- HEI-EUR — BUILDING_ACCELERATION — score 5.236/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAL-EUR — BUILDING_ACCELERATION — score 5.218/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MOODENG-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.716/10 — sources ACCELERATION — MEMORY_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 8.261/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- W-EUR — MEMORY_24H — score mémoire 7.838/10 — sources ACCELERATION — MEMORY_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.670/10 — sources ACCELERATION — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.625/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 7.606/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — MEMORY_24H — score mémoire 7.518/10 — sources ACCELERATION — MEMORY_ONLY
- STRK-EUR — MEMORY_24H — score mémoire 7.490/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +37.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALT-EUR +33.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BILL-EUR +29.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +18.74% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DYM-EUR +14.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRIA-EUR +13.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IOST-EUR +13.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PARTI-EUR +12.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +12.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ORCA-EUR +11.54% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
