import json
import sys
from base_annotator import Annotator, AnnotationType
from ROBCOLLOB_MoveTest import pickup_action, point_action, pick_up_and_move_block, point_action_new

class ActionAnnotator(Annotator):
    def initialize(self):
        super(ActionAnnotator, self).initialize()
        self.annotation_types.append(ActionAnnotation.ANNOTATION_UIMA_TYPE_NAME)

    def process(self, cas):
        x_location = cas['_views']['_InitialView']['CoordinateTransformation'][0]['x']
        y_location = cas['_views']['_InitialView']['CoordinateTransformation'][0]['y']
        doAction = cas['_views']['_InitialView']['ConfidenceFeedback'][0]['feedbackMsg']
        print(doAction)
        if(doAction == "true"):
            print("action True")
            pick_up_and_move_block(x_location, y_location)
        else:
            print("action False")
            point_action_new(x_location, y_location)

        annotation = ActionAnnotation()
        self.add_annotation(annotation)

class ActionAnnotation(AnnotationType):
    ANNOTATION_UIMA_TYPE_NAME = "edu.rosehulman.aixprize.pipeline.types.Action"
    
    def __init__(self):
        self.name = self.ANNOTATION_UIMA_TYPE_NAME
