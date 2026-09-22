# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T00:00:48.541417+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WAL-EUR | action ACHETE_MAINTENANT | opportunité 8.805 | entrée 6.900 | trend 9.200 | rang 8.303
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.101 | entrée 6.100 | trend 8.650 | rang 7.812
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BIGTIME-EUR | action LATENT_ACCELERATOR | opportunité 7.642 | entrée 4.500 | trend 8.450 | rang 7.331
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.617 | entrée 6.750 | trend 8.950 | rang 8.169
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.303
2. AERO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.293
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.169

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 7.959/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CROSS-EUR — CONFIRMED_ACCELERATION — score 7.285/10 — DETECTED_BUT_TOO_LATE
- TAO-EUR — CONFIRMED_ACCELERATION — score 6.811/10 — DETECTED_BUT_TOO_LATE
- RENDER-EUR — BUILDING_ACCELERATION — score 5.752/10 — DETECTED_BUT_TOO_LATE
- WCT-EUR — BUILDING_ACCELERATION — score 5.067/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — BUILDING_ACCELERATION — score 4.971/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RUNE-EUR — BUILDING_ACCELERATION — score 4.919/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.303/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.293/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.169/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +80.07% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +77.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +53.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +43.65% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SWELL-EUR +40.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FORM-EUR +35.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +31.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +29.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +23.93% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- WIF-EUR +21.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
