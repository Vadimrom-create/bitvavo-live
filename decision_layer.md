# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T06:00:30.744895+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PUMP-EUR | action ACHETE_MAINTENANT | opportunité 8.546 | entrée 8.100 | trend 8.350 | rang 7.926
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYDX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.187 | entrée 6.050 | trend 8.950 | rang 7.945
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : AUDIO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.016 | entrée 6.250 | trend 8.650 | rang 8.128
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. PUMP-EUR — ACHETE_MAINTENANT — rank 7.926 — opportunité 8.546 — entrée 8.100 — trend 8.350
2. AAVE-EUR — ACHETE_MAINTENANT — rank 7.907 — opportunité 8.153 — entrée 7.000 — trend 8.900
3. LTC-EUR — ACHETE_MAINTENANT — rank 7.502 — opportunité 8.868 — entrée 7.700 — trend 6.600
4. HYPE-EUR — ACHETE_MAINTENANT — rank 6.518 — opportunité 8.420 — entrée 7.700 — trend 4.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AUDIO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.128
2. DYDX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.945
3. PUMP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.926

## Accélération indépendante

- PARTI-EUR — CONFIRMED_ACCELERATION — score 8.518/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — CONFIRMED_ACCELERATION — score 7.103/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 6.194/10 — DETECTED_BUT_TOO_LATE
- C98-EUR — BUILDING_ACCELERATION — score 5.523/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — BUILDING_ACCELERATION — score 5.435/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BRETT-EUR — BUILDING_ACCELERATION — score 4.833/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PARTI-EUR — ACTIVE_NOW — score mémoire 8.518/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — ACTIVE_NOW — score mémoire 8.128/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.078/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.987/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +158.00% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +56.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +33.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +28.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +19.64% — DETECTED_EARLY — couche NONE — action NONE
- ALICE-EUR +14.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +12.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +11.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PONKE-EUR +11.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOS-EUR +10.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
