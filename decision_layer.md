# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T01:26:58.581501+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.151 | entrée 7.450 | trend 8.400 | rang 7.837
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.957 | entrée 6.300 | trend 8.650 | rang 7.770
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.837
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.770
3. ENA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 6.186

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SYN-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.107/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.050/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources ACCELERATION, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.837/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +47.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +44.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +38.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +24.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +22.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- APT-EUR +22.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +21.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +21.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +20.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +18.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
