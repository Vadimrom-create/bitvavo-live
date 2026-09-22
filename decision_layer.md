# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T14:56:20.538496+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 8.346 | entrée 7.800 | trend 8.100 | rang 7.841
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.108 | entrée 6.000 | trend 8.900 | rang 7.848
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.842 | entrée 5.450 | trend 8.550 | rang 7.399
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : 0G-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.205 | entrée 6.250 | trend 8.600 | rang 7.860
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. 0G-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.860
2. FLUX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.848
3. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.841

## Accélération indépendante

- AUDIO-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — BUILDING_ACCELERATION — score 6.301/10 — DETECTED_BUT_TOO_LATE
- POPCAT-EUR — BUILDING_ACCELERATION — score 5.487/10 — DETECTED_BUT_TOO_LATE
- GOAT-EUR — BUILDING_ACCELERATION — score 5.168/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUN-EUR — BUILDING_ACCELERATION — score 4.915/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 4.888/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — BUILDING_ACCELERATION — score 4.841/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — BUILDING_ACCELERATION — score 4.795/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- THE-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +87.93% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +65.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +31.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +26.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +25.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +17.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +17.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FORM-EUR +14.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +13.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +13.79% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
