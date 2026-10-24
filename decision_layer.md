# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-24T01:03:58.888323+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ELSA-EUR | action LATENT_ACCELERATOR | opportunité 8.032 | entrée 5.750 | trend 8.750 | rang 7.343
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.343

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 8.689/10 — DETECTED_BUT_TOO_LATE
- AXIS-EUR — CONFIRMED_ACCELERATION — score 7.606/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.976/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 6.587/10 — DETECTED_BUT_TOO_LATE
- IRYS-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — BUILDING_ACCELERATION — score 6.336/10 — DETECTED_BUT_TOO_LATE
- DOGS-EUR — BUILDING_ACCELERATION — score 6.327/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOS-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- WHUF-EUR — BUILDING_ACCELERATION — score 5.763/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DATAIP-EUR — BUILDING_ACCELERATION — score 5.383/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SYN-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 8.689/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CPOOL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.318/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 8.032/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 7.921/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.676/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — ACTIVE_NOW — score mémoire 7.606/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.343/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_DECAY_24_72H — score mémoire 7.261/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +265.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BIRB-EUR +240.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +96.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +29.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +27.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +24.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +22.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARK-EUR +22.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +20.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +20.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
