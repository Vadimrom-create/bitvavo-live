# Protocole SCAN — décision humaine contextualisée

Version 1 — 2026-10-08. Procédure de réponse à la commande conversationnelle **SCAN**. Ce document ne change **aucune** règle du scanner de production Solaire, des alertes, de l'exécution, des stops, des shadows ni des emails. Il ne déclenche pas d'ordre.

## Principe obligatoire

Chaque SCAN combine (1) les signaux quantitatifs et la liquidité réellement observés par Solaire/Bitvavo et (2) une **revue externe spontanée et actualisée du contexte macro, micro et des catalyseurs**. Jamais de recommandation d'achat à partir du score Solaire seul. Une revue macro non disponible doit être signalée explicitement ; ne pas faire comme si les actualités étaient vérifiées.

## Étapes de lecture

1. **Fraîcheur et fonctionnement.** Lire les derniers cycles `production_scan_status.json`, `production_alert_status.json`, `production_alert_candidates.json`, les observations d'exécution (carnets, frais, taille 100–150 €, spread), et les shadows pertinents. Distinguer horodatage des signaux, carnet et cours. Si données d'exécution trop anciennes, ne pas annoncer « achetable maintenant ». Le dépôt GitHub contient des instantanés et non une connexion Bitvavo interactive permanente.
2. **Régime crypto.** BTC/ETH/SOL (1 h, 4 h, 24 h), dominance et rotation si mesurables, breadth des altcoins, corrélations, volumes, liquidations et funding si sources fiables, pression acheteuse/vendeuse. Distinguer rebond technique et retournement confirmé. Si métrique absente, le dire.
3. **Macroéconomie vérifiée sur le web à CHAQUE SCAN.** Vérifier actualités récentes, Fed/BCE, taux et obligations, inflation, emploi, croissance, dollar, pétrole, tensions géopolitiques, annonces réglementaires, et calendrier économique des prochaines 24 h, 48 h, 72 h et de la semaine. Recouper calendrier sur sources officielles (Fed, BLS, BEA, Census, BCE, etc.) quand possible ; donner dates et heures France, type d'annonce, anticipation consensuelle si publiée et mécanisme de transmission possible. Une conférence ou des déclarations non programmées ne peuvent être présentées comme des échéances confirmées.
4. **Micro/catalyseurs sur candidats et rebonds.** Pour chacun des meilleurs candidats et des éventuelles cryptos récemment très corrigées : actualités officielles du projet, mises à jour, gouvernance, unlock/vesting, listing/delisting, incidents de sécurité, volume, profondeur, spread, structure graphique et force relative à BTC. Séparer actualité vérifiée, rumeur et absence de source. Une baisse importante seule n'est pas un avantage statistique.
5. **Scénarios conditionnels.** Décrire le scénario haussier et baissier pour les 24–72 h (et 7 j si pertinent), les événements qui pourraient les déclencher, et leurs conditions observables de confirmation / invalidation. Ne pas donner de probabilités chiffrées artificielles ou de prévisions de performance non calibrées.
6. **Décision actionnable.** Terminer par une réponse explicite : **ACHETER / ATTENDRE / PAS D'ACHAT**. Pour une proposition ACHETER : paire EUR, prix vérifié et heure, entrée limite ou zone, taille indicative 100–150 €, stop d'invalidation structurelle non artificiellement serré, niveau de prise partielle/objectif, coûts/spread, ce qui annulerait la thèse, et proximité des annonces. Sans carnet et validation de cours frais : **pas d'achat immédiat validé**. Un bon candidat peut être « ATTENDRE » lorsque la volatilité événementielle est défavorable ; ne pas transformer l'existence d'une annonce en veto systématique.
7. **Opportunités de rebond.** Inclure, si le marché vient de fortement corriger, au plus trois candidats distincts sous **SURVEILLANCE REBOND**. Les sélectionner par qualité fondamentale/catalyseur, liquidité, force relative et structure de reprise, pas seulement la magnitude de leur perte. Les distinguer nettement des achats autorisés par Solaire.

## Format compact par défaut

- **Verdict immédiat** (en une phrase et horaire de référence).
- **Marché maintenant** : régime, BTC et breadth.
- **Prochaines annonces susceptibles de déplacer le marché** : date/heure en Europe/Paris, impact potentiel haussier/baissier, sources.
- **Candidats Solaire** : rang, état, score, prix et fraîcheur, carnet et motif du feu vert/attente/refus.
- **Surveillance rebond** (si pertinente) : jusqu'à 3 actifs, catalyseur, déclencheur et invalidation.
- **Deux scénarios** et **décision concrète** en une ligne.

## Contraintes et traçabilité

La stratégie cible des mouvements de 24–48–72 h à 1 semaine, non le bruit de 5–10 minutes. Les événements doivent être datés et sourcés. Toute donnée passée, indirecte, incomplète ou non actualisable doit être désignée comme telle. Ne pas inventer un carnet Bitvavo temps réel à partir d'un snapshot GitHub. Ne pas promettre une exhaustivité sur « tout le contexte » : rechercher systématiquement les facteurs *matériellement pertinents* à la décision. Consigner, quand utile, une hypothèse d'entrée qui puisse être confrontée aux shadows ; ne pas en déduire une causalité ou un avantage non démontrés.

**Périmètre** : protocole des réponses conversationnelles à « SCAN ». Il ne constitue pas un veto machine, un ordre automatique, un service de veille permanente ni une modification de la production Solaire.
