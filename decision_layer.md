# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T19:44:23.085418+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 7.476 | entrée 7.000 | trend 8.000 | rang 7.380
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYDX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.408 | entrée 6.200 | trend 8.700 | rang 7.473
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.716 | entrée 4.300 | trend 9.200 | rang 8.072
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.319 | entrée 5.900 | trend 9.200 | rang 8.087
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 7.380 — opportunité 7.476 — entrée 7.000 — trend 8.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.087
2. KSM-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.072
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.037

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.692/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALICE-EUR — CONFIRMED_ACCELERATION — score 8.163/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — CONFIRMED_ACCELERATION — score 7.219/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.759/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — BUILDING_ACCELERATION — score 4.989/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — BUILDING_ACCELERATION — score 4.849/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COTI-EUR — BUILDING_ACCELERATION — score 4.801/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 4.791/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.692/10 — sources ACCELERATION, V4 — WATCH_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ALICE-EUR — ACTIVE_NOW — score mémoire 8.163/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.063/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +133.92% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +70.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +34.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +27.06% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MEGA-EUR +26.63% — DETECTED_EARLY — couche NONE — action NONE
- GTC-EUR +24.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +21.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VELO-EUR +20.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +19.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVE-EUR +18.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
