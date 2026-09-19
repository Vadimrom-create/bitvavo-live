# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T11:17:27.360546+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.791 | entrée 7.950 | trend 7.650 | rang 7.783
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.718 | entrée 4.500 | trend 8.250 | rang 7.282
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.842 | entrée 6.250 | trend 8.750 | rang 7.905
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.905
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.783
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.776

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 7.593/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.288/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.199/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.093/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.045/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +40.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +39.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +34.53% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +33.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +31.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +31.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +28.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +25.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +25.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +24.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
