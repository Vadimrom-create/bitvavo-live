# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T17:21:16.615207+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 9.112 | entrée 8.150 | trend 7.400 | rang 7.924
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.413 | entrée 4.500 | trend 8.050 | rang 6.992
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.986 | entrée 6.250 | trend 8.750 | rang 7.772
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.924
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.772
3. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.693

## Accélération indépendante

- PEPE-EUR — CONFIRMED_ACCELERATION — score 8.866/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 8.169/10 — DETECTED_BUT_TOO_LATE
- DOGE-EUR — BUILDING_ACCELERATION — score 4.898/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 8.866/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.334/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.225/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — ACTIVE_NOW — score mémoire 8.169/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ATH-EUR — ACTIVE_NOW — score mémoire 8.101/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.021/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.942/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +41.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +36.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +29.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +27.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +25.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +22.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +21.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- G-EUR +19.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +18.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
