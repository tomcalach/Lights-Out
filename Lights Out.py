def lights_out(on_panels):
    """
    lights_out gives a solution (not necessarily the best), to any given state of the board in the game Lights Out.
    It takes the state of the board as list of numbers, indicating the squares which are lighten up. It returns a list
    of number on which the player should press in order to solve the game.
    :param on_panels: list of unique numbers between 1 and 25
    :return: list of unique numbers between 1 and 25
    """
    def lights_off(lights_list):
        """
        lights_off is implementing the first round of the algorithm. It goes through the list and "press" on the next
        button on the row below the smallest number. This way it is systematically turn off all the lights except the
        last row. The function returns a tuple of two objects; first object is a list of all the buttons needed to be
        pressed in order to give back a clean board except the last row, the second is a sorted list of the buttons
        which are still lightning in the last row.
        :param lights_list: list of unique integers between 1 and 25
        :return: tuple of length 2, first object is a list of unique integers between 1 and 20, second object is a list
        of unique integers between 21 and 25.
        """
        press_list = []
        while lights_list:
            light = min(lights_list)
            if light > 20:
                break

            press = light + 5
            press_list.append(press)
            lights_list.remove(press - 5)
            for light_to_be_turned in [press, press - 1, press + 1, press + 5]:
                # If the pressed button "press" is in the left then there is no button to the left of it, so the one
                # smaller button shouldn't be turned. The same is valid to the right end or to the last row (with
                # different buttons to be excluded)
                if (light_to_be_turned % 5 == 1 and press % 5 == 0) or (light_to_be_turned % 5 == 0 and press % 5 == 1)\
                        or light_to_be_turned > 25:
                    continue
                else:
                    if light_to_be_turned in lights_list:
                        lights_list.remove(light_to_be_turned)
                    elif light_to_be_turned > 0:
                        lights_list.append(light_to_be_turned)
        return press_list, sorted([x for x in lights_list if x > 20])

    def second_round(last_row_position):
        """
        second_round is receiving the list of the lights left in the last row, each of this states got a define
        solution to the game; For it to take place 1/2 buttons (corresponding to the last row state) should be pressed,
        and the algorithm implemented in the function lights_off is running again, and gives a plain board in the end.
        So the list provided by it is the complementary part for the first round list, the addition of both will give
        the answer to the problem.
        :param last_row_position: list of unique integers between 21 and 25.
        :return: list of unique integers between 1 and 25.
        """
        if last_row_position == [21, 25]:
            second_round_presses, noting = lights_off([-4, -3])
        elif last_row_position == [22, 24]:
            second_round_presses, noting = lights_off([-4, -1])
        elif last_row_position == [21, 22, 23]:
            second_round_presses, noting = lights_off([-3])
        elif last_row_position == [23, 24, 25]:
            second_round_presses, noting = lights_off([-1])
        elif last_row_position == [21, 23, 24]:
            second_round_presses, noting = lights_off([0])
        elif last_row_position == [22, 23, 25]:
            second_round_presses, noting = lights_off([-4])
        elif last_row_position == [21, 22, 24, 25]:
            second_round_presses, noting = lights_off([-2])
        return second_round_presses

    presses, last_row = lights_off(on_panels)
    presses.extend(second_round(last_row))

    return presses





