# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T01:37:51.683203+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.897 | entrée 4.950 | trend 9.200 | rang 7.768
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.768
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.369
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.303

## Accélération indépendante

- UNI-EUR — BUILDING_ACCELERATION — score 5.707/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- SUI-EUR — BUILDING_ACCELERATION — score 4.984/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.657/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.395/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.361/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.927/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +76.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +33.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +25.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRAC-EUR +19.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +18.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +17.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +17.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +16.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +16.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +14.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
