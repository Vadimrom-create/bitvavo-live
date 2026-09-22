# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T08:18:20.114277+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVNT-EUR | action ACHETE_MAINTENANT | opportunité 9.186 | entrée 7.400 | trend 8.100 | rang 8.270
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LISTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.151 | entrée 5.800 | trend 8.500 | rang 7.680
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : THE-EUR | action LATENT_ACCELERATOR | opportunité 7.799 | entrée 5.100 | trend 8.700 | rang 7.550
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.120 | entrée 7.500 | trend 7.750 | rang 7.767
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AVNT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.270
2. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.156
3. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.117

## Accélération indépendante

- USELESS-EUR — CONFIRMED_ACCELERATION — score 9.245/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 6.354/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 6.148/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — BUILDING_ACCELERATION — score 6.101/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PLUME-EUR — BUILDING_ACCELERATION — score 5.455/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIF-EUR — BUILDING_ACCELERATION — score 5.404/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.230/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 5.009/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VTHO-EUR — BUILDING_ACCELERATION — score 4.840/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ORCA-EUR — BUILDING_ACCELERATION — score 4.783/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.367/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 9.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.979/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 8.270/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +109.98% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +88.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +48.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +38.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +27.19% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +25.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +24.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +22.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +20.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CARV-EUR +20.09% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
