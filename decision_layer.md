# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T19:25:18.685052+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVAX-EUR | action ACHETE_MAINTENANT | opportunité 8.229 | entrée 7.600 | trend 8.700 | rang 7.980
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GALA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.641 | entrée 6.400 | trend 8.450 | rang 7.446
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.093 | entrée 5.200 | trend 9.200 | rang 7.890
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.093 | entrée 6.900 | trend 8.900 | rang 7.950
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AVAX-EUR — ACHETE_MAINTENANT — rank 7.980 — opportunité 8.229 — entrée 7.600 — trend 8.700
2. HUMA-EUR — ACHETE_MAINTENANT — rank 7.718 — opportunité 7.847 — entrée 6.800 — trend 8.550
3. LINK-EUR — ACHETE_MAINTENANT — rank 7.679 — opportunité 8.095 — entrée 7.600 — trend 8.000
4. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.584 — opportunité 7.851 — entrée 6.900 — trend 8.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.980
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.950
3. KSM-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.890

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 8.063/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — CONFIRMED_ACCELERATION — score 7.386/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — BUILDING_ACCELERATION — score 4.891/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 8.063/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARPA-EUR — MEMORY_DECAY_24_72H — score mémoire 7.976/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +137.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +73.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +29.85% — DETECTED_EARLY — couche NONE — action NONE
- CAP-EUR +28.98% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALICE-EUR +28.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +22.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +21.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +19.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +19.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +17.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
