# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T12:52:58.846770+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : W-EUR | action ACHETE_MAINTENANT | opportunité 9.302 | entrée 7.400 | trend 8.650 | rang 8.344
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.520 | entrée 6.150 | trend 8.900 | rang 7.887
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SKY-EUR | action LATENT_ACCELERATOR | opportunité 7.869 | entrée 4.500 | trend 8.450 | rang 7.383
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.399 | entrée 7.200 | trend 8.650 | rang 8.438
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. W-EUR — ACHETE_MAINTENANT — rank 8.344 — opportunité 9.302 — entrée 7.400 — trend 8.650
2. FET-EUR — ACHETE_MAINTENANT — rank 8.034 — opportunité 9.060 — entrée 7.600 — trend 7.900
3. XDC-EUR — ACHETE_MAINTENANT — rank 7.985 — opportunité 8.231 — entrée 7.000 — trend 9.000
4. ONDO-EUR — ACHETE_MAINTENANT — rank 7.938 — opportunité 9.127 — entrée 7.550 — trend 7.750
5. KAS-EUR — ACHETE_MAINTENANT — rank 7.882 — opportunité 8.116 — entrée 7.150 — trend 8.700
6. SEI-EUR — ACHETE_MAINTENANT — rank 7.878 — opportunité 8.247 — entrée 7.600 — trend 8.850
7. BCH-EUR — ACHETE_MAINTENANT — rank 7.822 — opportunité 8.957 — entrée 7.150 — trend 7.550
8. LINK-EUR — ACHETE_MAINTENANT — rank 7.775 — opportunité 8.776 — entrée 6.850 — trend 8.550
9. ADA-EUR — ACHETE_MAINTENANT — rank 7.416 — opportunité 8.895 — entrée 7.150 — trend 7.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.438
2. W-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.344
3. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.034

## Accélération indépendante

- PUMP-EUR — CONFIRMED_ACCELERATION — score 7.323/10 — DETECTED_BUT_TOO_LATE
- BICO-EUR — CONFIRMED_ACCELERATION — score 6.664/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 6.331/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROVE-EUR — BUILDING_ACCELERATION — score 6.270/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — BUILDING_ACCELERATION — score 6.071/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 6.045/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.913/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — BUILDING_ACCELERATION — score 5.696/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — BUILDING_ACCELERATION — score 5.444/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — BUILDING_ACCELERATION — score 5.127/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LINK-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- POL-EUR — ACTIVE_NOW — score mémoire 6.827/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — MEMORY_24H — score mémoire 9.914/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARX-EUR — MEMORY_24H — score mémoire 9.471/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.438/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.344/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +44.97% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +26.53% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +16.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +16.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +12.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +10.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IKA-EUR +10.59% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ALGO-EUR +10.56% — DETECTED_EARLY — couche NONE — action NONE
- AZTEC-EUR +10.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +10.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
