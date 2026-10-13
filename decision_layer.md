# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-13T02:47:54.494365+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PYTH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.440 | entrée 6.650 | trend 8.200 | rang 7.035
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.694 | entrée 7.000 | trend 8.550 | rang 7.404
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.404
2. PYTH-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.035
3. CHIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.916

## Accélération indépendante

- CT-EUR — CONFIRMED_ACCELERATION — score 7.250/10 — DETECTED_BUT_TOO_LATE
- TIA-EUR — CONFIRMED_ACCELERATION — score 6.501/10 — DETECTED_BUT_TOO_LATE
- FORM-EUR — BUILDING_ACCELERATION — score 6.139/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — BUILDING_ACCELERATION — score 5.469/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — BUILDING_ACCELERATION — score 5.445/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARPA-EUR — BUILDING_ACCELERATION — score 5.400/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RAD-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- STRK-EUR — MEMORY_24H — score mémoire 8.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.696/10 — sources ACCELERATION — MEMORY_ONLY
- DBR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.417/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- SXT-EUR — MEMORY_24H — score mémoire 8.267/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 7.878/10 — sources ACCELERATION — MEMORY_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 7.776/10 — sources ACCELERATION — MEMORY_ONLY
- GRASS-EUR — MEMORY_24H — score mémoire 7.726/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAY-EUR — MEMORY_24H — score mémoire 7.600/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +35.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +31.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +28.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RSR-EUR +24.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKL-EUR +17.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RENDER-EUR +6.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +6.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DODO-EUR +5.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAFE-EUR +4.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +4.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
