# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-05T02:16:31.439296+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
Aucun candidat ne remplit actuellement un bucket décisionnel.

## Accélération indépendante

- EDGE-EUR — CONFIRMED_ACCELERATION — score 9.632/10 — DETECTED_BUT_TOO_LATE
- ESP-EUR — CONFIRMED_ACCELERATION — score 7.492/10 — DETECTED_BUT_TOO_LATE
- DATAIP-EUR — CONFIRMED_ACCELERATION — score 6.845/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 5.979/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.970/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CFG-EUR — BUILDING_ACCELERATION — score 5.575/10 — DETECTED_BUT_TOO_LATE
- ID-EUR — BUILDING_ACCELERATION — score 5.069/10 — DETECTED_BUT_TOO_LATE
- XTZ-EUR — BUILDING_ACCELERATION — score 5.054/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRV-EUR — BUILDING_ACCELERATION — score 4.955/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — ACTIVE_NOW — score mémoire 9.632/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ADX-EUR — MEMORY_24H — score mémoire 9.096/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.951/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_DECAY_24_72H — score mémoire 8.852/10 — sources ACCELERATION — MEMORY_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 8.560/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 7.995/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 7.864/10 — sources ACCELERATION — MEMORY_ONLY
- JTO-EUR — MEMORY_24H — score mémoire 7.710/10 — sources ACCELERATION — MEMORY_ONLY
- ESP-EUR — ACTIVE_NOW — score mémoire 7.492/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ELSA-EUR +48.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDGE-EUR +46.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +31.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +28.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +25.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +21.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAY-EUR +17.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +17.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PTB-EUR +17.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +17.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
