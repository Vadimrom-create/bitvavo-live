# Solaire — Pré-engagement prospectif sur les carnets de sortie (12 octobre 2026)

**PR #163 : recherche uniquement — aucune modification de production.**

## État concret, source et engagements

Le 12 octobre 2026 à **18:01:00 UTC** (20:01 Paris), avant toute observation des sorties à venir, nous avons inscrit **81 échéances de contrôle futures** pour **26 marchés EUR** dans `research/PROSPECTIVE_EXIT_BOOK_TARGETS_20261012.json`. Source : journal public machine `production_direct_decision_journal.json`, version Git blob `b524f59dfa349d65457889548411bd666e05f75e`, publication du journal à 17:32:13 UTC. Cette sélection ne dépend **ni de résultats postérieurs ni de fortes hausses du lendemain**.

Les 81 lignes sont toutes des décisions machine `BUY_SENT` ayant un plan cohérent, et des temps pré-engagés `decision_ts + 4 h / 12 h / 24 h` (signal âgé de X heures). Première échéance : 2026-10-12 18:20:56 UTC ; dernière : 2026-10-13 17:32:11 UTC. Les identifiants et horizons sont figés par commit. Nous travaillons sur la **population de signaux**, pas des achats personnels ni même des ordres papier exécutés. Un BUY_SENT n'établit ni achat confirmé ni position encore ouverte après X heures.

## Instrumentation research-only

- `scripts/capture_precommitted_exit_books.py` : avant chaque appel, vérifier l'existence de la ligne **déjà engagée** et sa date. Seules les cibles dont l'échéance vient de passer sont interrogées. Les observations postérieures à **120 secondes** ne reçoivent pas le label « carnet de sortie à l'heure prévue ». Les cibles futures = `NOT_YET_DUE` ; anciennes manquées = `MISSED_CAPTURE_WINDOW`, sans données inventées.
- L'API est exclusivement la route publique `GET /v2/{market}/book?depth=1000`. Aucune authentification privée, aucun ordre, aucune position du wallet.
- Le rapport conserve le carnet brut, l'empreinte SHA-256, le début/fin de requête, l'heure exacte de disponibilité, le décalage par rapport à l'échéance, bid/ask, spread, validation ordonnée du carnet et **estimation de vente nominale de 100/150 € sur les niveaux acheteurs visibles**. Frais conventionnels 0,25 % et glissement additionnel 0,10 % lors de la vente **uniquement si le carnet est suffisamment profond**.
- La quantité « 100 EUR / meilleur bid » est une convention normalisée pour tester la **profondeur** et non la quantité détenue. Même lorsque le carnet affiche un bid exécutable, un ordre hypothétique ne serait pas garanti à ce prix après latence, annulation ou priorité dans la file.
- Aucun PnL réellement exécutable, aucun bénéfice mensuel, aucun drawdown liquidable ne doivent être déclarés à partir de ce test. `actual_wallet_pnl_eur=null` et `real_exit_fills_verified=0` sont invariant de l'outil.
- Limites d'API strictes : au plus 8 requêtes publiques par exécution et 120 secondes de tolérance. Les cibles ignorées à cause de capacité sont `CAPACITY_NOT_CAPTURED`, non pas des opportunités invalidées.

## Exécution et limitation majeure de cadence

Le workflow `.github/workflows/research_prospective_exit_books.yml` est déclenché **uniquement sur la PR ou manuellement**. Il exécute les tests, valide les 81 pré-engagements, réalise une prise de carnet opportuniste si une échéance est effectivement due **dans sa fenêtre de 120 secondes**, et archive l'ensemble des statuts dans un artifact CI 14 jours.

**Cela n'est PAS une surveillance périodique active.** Un workflow déclenché lors d'une PR ne garantit en rien une requête à l'une des 81 heures futures. GitHub n'exécute les workflows `schedule` que depuis la branche par défaut : tant que le code reste en draft sur une branche isolée et non fusionnée, **aucune collecte régulière n'est en service**. Toute échéance non observée dans la fenêtre doit être classée manquée, même si on retrouve un carnet dix minutes plus tard.

Pour rendre l'enquête véritablement prospective et produire un échantillon exploitable, il faudra un mode de déclenchement **hors production**, régulier ou basé sur les échéances pré-engagées, avec horaires vérifiables et archive durable. Cette opération distincte doit préserver intégralement les règles et les secrets de la production et ne doit jamais envoyer d'ordre.

## Comparaison économique et caveats

Ce premier pré-engagement porte sur `SOLAIRE_MACHINE_BUY_SENT` **uniquement**. Il ne représente ni V4 ni R2. Une comparaison causalement valable devra pré-engager des jeux de décisions V4/R2/témoin au **même instant**, mesurer les livres avant/après sortie, appliquer les mêmes frais et les mêmes 2 300 € de cash, et reporter séparément la non-exécution.

**Décision D inchangée : NO GO.** Ce programme ne modifie ni le scanner en production, ni les seuils, stops, e-mails, cryptos tenues, ni les ordres.
