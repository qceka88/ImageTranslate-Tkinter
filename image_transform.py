import cv2
import imutils
import numpy as np


class ImageTransform:

    def __init__(self, input_image):
        self.input_image = cv2.imread(input_image)
        self.temporary_image = None
        self.screen_contours = None
        self.process_image()

    def process_image(self):
        ratio = self.input_image.shape[0] / 500.0
        resized_image = imutils.resize(self.input_image, height=500)
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        self.temporary_image = cv2.Canny(blur_image, 75, 200)

        self.find_contours()
        self.draw_control_points_for_check(resized_image)

        self.temporary_image = self.image_transformation(self.input_image, self.screen_contours.reshape(4, 2) * ratio)
        self.temporary_image = cv2.cvtColor(self.temporary_image, cv2.COLOR_BGR2GRAY)

    def find_contours(self):
        contours = cv2.findContours(self.temporary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        sorted_contours = sorted(contours[0], key=cv2.contourArea, reverse=True)[:5]

        for contour in sorted_contours:
            perimeter = cv2.arcLength(contour, True)
            approximation = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

            if len(approximation) == 4:
                self.screen_contours = approximation
                break

    def draw_control_points_for_check(self, image):
        for point in self.screen_contours:
            cv2.circle(image, tuple(*point), 3, (0, 0, 255), 4)
        cv2.imshow('Check Corners Match', image)
        cv2.waitKey(0)

    def image_transformation(self, image, points):
        rect = self.order_points(points)
        (ul, ur, dl, dr) = rect

        width_a = np.sqrt(((dr[0] - dl[0]) ** 2) + ((dr[1] - dl[1]) ** 2))
        width_b = np.sqrt(((ur[0] - ul[0]) ** 2) + ((ur[1] - ul[1]) ** 2))

        height_a = np.sqrt(((ur[0] - dr[0]) ** 2) + ((ur[1] - dr[1]) ** 2))
        height_b = np.sqrt(((ul[0] - dl[0]) ** 2) + ((ul[1] - dl[1]) ** 2))

        max_width = max(int(width_a), int(width_b))
        max_height = max(int(height_a), int(height_b))

        destination = np.array([
            [0, 0],
            [max_width - 1, 0],
            [max_width - 1, max_height - 1],
            [0, max_height - 1]], dtype='float32'
        )
        matrix = cv2.getPerspectiveTransform(rect, destination)
        warped = cv2.warpPerspective(image, matrix, (max_width, max_height))

        return warped

    def order_points(self, points):
        rect = np.zeros((4, 2), dtype="float32")

        s = points.sum(axis=1)
        rect[0] = points[np.argmin(s)]
        rect[2] = points[np.argmax(s)]

        diff = np.diff(points, axis=1)
        rect[1] = points[np.argmin(diff)]
        rect[3] = points[np.argmax(diff)]

        return rect

    def return_result(self):
        return self.temporary_image
