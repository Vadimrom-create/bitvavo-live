# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T23:46:30.967989+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.036 | entrée 6.300 | trend 8.750 | rang 7.828
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.828
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.751
3. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.577

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 5.197/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZK-EUR — ACTIVE_NOW — score mémoire 8.286/10 — sources V4 — WATCH_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.948/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.940/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.932/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETC-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +43.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +39.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +38.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +26.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +24.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +23.64% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ENA-EUR +21.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INJ-EUR +18.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +14.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +13.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
