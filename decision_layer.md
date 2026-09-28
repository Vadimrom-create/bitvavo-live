# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T21:50:51.937170+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : XLM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.589 | entrée 6.750 | trend 8.450 | rang 7.583
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AZTEC-EUR | action LATENT_ACCELERATOR | opportunité 7.768 | entrée 5.550 | trend 8.900 | rang 7.648
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.893 | entrée 6.700 | trend 8.300 | rang 8.051
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.051
2. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.851
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.849

## Accélération indépendante

- NMR-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — CONFIRMED_ACCELERATION — score 9.275/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.276/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DATAIP-EUR — BUILDING_ACCELERATION — score 5.206/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- NMR-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — ACTIVE_NOW — score mémoire 9.275/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 7.972/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.849/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +34.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +28.96% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +13.32% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +12.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +9.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +9.38% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LINK-EUR +8.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +6.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +5.57% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOON-EUR +5.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
