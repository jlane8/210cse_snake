from game.scripting.action import Action

class MoveActorsAction(Action):
    
# TODO: Implement MoveActorsAction class here! 
    def execute(self, cast, script):
        """

        """
        self._actors = cast.get_all_actors()
        self._actions = script.get_actions("snakes")
        for actor in self._actors:
            actor.move_next()
        return 
# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor