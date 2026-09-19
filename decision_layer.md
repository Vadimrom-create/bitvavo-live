# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T17:59:33.447071+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 9.100 | entrée 7.750 | trend 7.400 | rang 7.951
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.493 | entrée 4.500 | trend 8.050 | rang 7.101
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.455 | entrée 6.800 | trend 8.950 | rang 8.038
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.038
2. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.951
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.799

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.410/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VET-EUR — ACTIVE_NOW — score mémoire 8.314/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.215/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — ACTIVE_NOW — score mémoire 8.154/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.081/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.038/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.951/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +39.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +36.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +32.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +29.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +26.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +25.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +21.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +18.42% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +16.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALLO-EUR +16.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
