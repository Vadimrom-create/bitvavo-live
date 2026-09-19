# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T10:57:49.476246+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.769 | entrée 7.600 | trend 6.950 | rang 7.548
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : RAY-EUR | action LATENT_ACCELERATOR | opportunité 7.503 | entrée 4.500 | trend 8.300 | rang 7.002
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.352 | entrée 6.600 | trend 8.750 | rang 7.845
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.845
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.810
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.691

## Accélération indépendante

- ZAMA-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- APT-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- SUI-EUR — ACTIVE_NOW — score mémoire 7.442/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- WAL-EUR — ACTIVE_NOW — score mémoire 8.345/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.261/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.248/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 7.917/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ZAMA-EUR +46.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +43.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +34.74% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +30.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +29.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +27.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +27.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +25.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +24.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +24.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
