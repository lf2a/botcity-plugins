import os

from botcity.plugins.cloudvision import BotCloudVisionPlugin

PROJECT_PATH = os.path.abspath('')
CREDENTIALS = os.path.join(PROJECT_PATH, 'credentials.json')


def read_image(image_path, credentials):
    cloudvision = BotCloudVisionPlugin()
    cloudvision.credentials(credentials)
    cloudvision.read(image_path)
    print(cloudvision.entries())  # get position of elements
    return cloudvision.full_text()


if __name__ == '__main__':
    text = read_image(os.path.join(PROJECT_PATH, 'image.jpg'), CREDENTIALS)
    print(text)

    # Output:
    # [['When', 212, 8, 439, 8, 439, 71, 212, 71, 1], ['you', 458, 24, 599, 24, 599, 83, 458, 83, 1], ['switch', 620, 8, 879, 8, 879, 71, 620, 71, 1], ['from', 166, 90, 351, 92, 350, 154, 165, 152, 1], ['C++', 374, 82, 525, 84, 524, 152, 373, 150, 1], ['to', 550, 97, 627, 98, 626, 153, 549, 152, 1], ['Python', 650, 88, 925, 91, 924, 170, 649, 167, 1], ['Thanks', 350, 526, 617, 540, 613, 613, 346, 599, 1], ['guys', 643, 549, 804, 557, 800, 620, 640, 612, 1], ['pointers', 176, 750, 317, 753, 316, 792, 175, 789, 1], ['main()', 690, 808, 795, 807, 795, 840, 690, 841, 1], ['{', 588, 833, 619, 833, 619, 867, 588, 867, 1], ['}', 627, 829, 634, 829, 634, 875, 627, 875, 1], ['++', 311, 872, 349, 871, 350, 889, 312, 890, 1], ['So', 275, 1014, 363, 1015, 363, 1079, 275, 1078, 1], ['long,', 367, 1014, 515, 1015, 515, 1080, 367, 1079, 1], ['partner', 486, 1015, 729, 1017, 729, 1080, 486, 1078, 1]]
    #
    # When you switch
    # from C++ to Python
    # Thanks guys
    # pointers
    # main()
    # { }
    # ++
    # So long, partner


# Possiveis erros:
# ValueError: Service account info was not in the expected format, missing fields token_uri, client_email.
# Para resolver esse problema crie uma conta de serviço

# Enable billing
# Para usar o cloud vision é necessário ativar a conta de faturamento e vincular ao projeto.
