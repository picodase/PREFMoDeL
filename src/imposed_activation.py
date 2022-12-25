# Method: Imposed activation: returns 3 features
## FEATURE : Imposed activation product set (IAPS)
## FEATURE : Imposed activation product tree (IAPT)
## FEATURE : Reactive trajectory set (IARTS)

# The reaction search consists of the four steps below, followed by post-processing of obtained reaction trajectories.
# 1. The initial structure of the reactants is optimized, and the user selects a reactive coordinate q (i.e., an interatomic distance, a bending angle, or a torsional angle). With the reactive coordinate fixed at its equilibrium value q0, an initial conformer search is performed to obtain a diverse set of structures. A relaxed scan of the reactive coordinate follows, starting with one of the initially generated conformers, to an intermediate value between that of reactants and products qi.
# 2. A second, shorter and less exhaustive conformer search is undertaken with the reactive coordinate constrained at qi to explore the local energy landscape.
# 3. All the structures thereby generated are scanned from q = qi to qN to obtain new reaction products. A backward scan from qi to q0 yields a complete trajectory back to a reactant conformation.

class Coordinate:
    def determine_form():
        coordtype = {
            2: 'distance',
            3: 'angle',
            4: 'dihedral'
        }
        self.form = coordtype[len(self.atoms)]
        return

    def __init__(self, atoms:list):
        self.atoms = atoms
        return

class ImposedActivation:
    def __init__():
        return

    def ReactionSearch(structure0:MDAnalysis.Universe=s0,
                            coord:Coordinate=cd, rceqv:float=q0) -> tuple:
        '''
    DESCRIPTION

        Performs an imposed activation reaction search.

    PARAMETERS

        structure0  :   Initial structure of the reaction system
        coord       :   The reactive coordinate
        rceqv       :   The reactive coordinate's equilibrium value

    RETURNS

        iaps        :   Imposed activation product set
        iapt        :   Imposed activation product tree
        trajset     :   Set of trajectories along which each reaction occurs
        '''

        def optimize_structure(structure:MDAnalysis.Universe=s0) -> MDAnalysis.Universe:
            '''
            Optimizes an input structure to a low energy
            '''
            return None

        s0 = optimize_structure(s0)  # Optimize initial structure
        q = q0  # Set reactive coordinate to its equilibrium value

        def conformer_search(structure:MDAnalysis.Universe=s) -> list:
            '''
            Runs a conformer search and returns a list of conformers
            '''
            return

        # Run initial conformer search
        cs = conformer_search(s0)

        def relaxed_scan(structure:MDAnalysis.Universe=s, coord:Coordinate=c) -> Float:
            '''
            Performs a relaxed scan along a coordinate of an input structure

        RETURNS

            qk  :   Float   An intermediate position along the reaction coordinate
            '''
            qk = None

            return qk

        qks = []

        # For several initially generated conformers,
        # Perform relaxed scan of the reactive coordinate
        qks = [relaxed_scan(structure=c, coord=coord) for c in cs]
        # TODO: Observe/set criteria to select intermediate value reached between q0 and qi


        # For 100 steps, recursively (?)
            # Perform a second, shorter and less exhaustive conformer search, using the reactive coordinate constrained at qi to explore the local energy landscape.

            # TODO: Include assumption that cross reactions can occur;
                # i.e. add probability of reacting with surrounding products after traversing the full reaction tree with products generated after initial products were formed
            # Scan all generated structures from q = qi to qN to obtain new reaction products
            # Run a backward scan from qi to q0 and get a complete inverse trajectory

            # Optimize structures of energy minima (potential reactants and products) without constraints to ensure stability.


        # Assemble the resulting set of trajectories into a tree data structure
        iapt = None
        iaps = set(iapt)
        trajset = None

        return (iapt, iaps, trajset)

    def IAPostProcessing():
        '''
        Performs postprocessing on an imposed activation reaction tree
        '''

        return