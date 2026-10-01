# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T20:21:54.927037+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.240 | entrée 7.550 | trend 8.400 | rang 8.321
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PROM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.756 | entrée 6.650 | trend 8.700 | rang 7.721
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TRAC-EUR | action LATENT_ACCELERATOR | opportunité 8.465 | entrée 5.550 | trend 8.950 | rang 7.718
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.225 | entrée 6.450 | trend 9.200 | rang 8.087
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.321 — opportunité 9.240 — entrée 7.550 — trend 8.400
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.258 — opportunité 8.719 — entrée 7.650 — trend 8.900
3. AVAX-EUR — ACHETE_MAINTENANT — rank 7.914 — opportunité 8.068 — entrée 7.350 — trend 8.700
4. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.847 — opportunité 8.482 — entrée 6.950 — trend 8.500
5. SUI-EUR — ACHETE_MAINTENANT — rank 7.771 — opportunité 8.010 — entrée 7.600 — trend 8.400
6. PUMP-EUR — ACHETE_MAINTENANT — rank 7.668 — opportunité 8.239 — entrée 6.800 — trend 8.500
7. LINK-EUR — ACHETE_MAINTENANT — rank 7.418 — opportunité 7.553 — entrée 7.350 — trend 8.000
8. LTC-EUR — ACHETE_MAINTENANT — rank 6.945 — opportunité 8.549 — entrée 7.250 — trend 5.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.321
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.258
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.087

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 8.002/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALICE-EUR — CONFIRMED_ACCELERATION — score 6.968/10 — DETECTED_BUT_TOO_LATE
- TLM-EUR — BUILDING_ACCELERATION — score 5.843/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 5.599/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.247/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.321/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.258/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.063/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.002/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +150.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +66.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +40.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +26.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +25.61% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MEGA-EUR +23.63% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +21.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +18.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +18.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +18.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
