from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import MessageHandler, filters
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

                                                  #CLASS UNITCONVERTER

class UnitConverter:
    def __init__(self):
        pass
 #conversion functions

    def miles_to_km(self, miles):
        return miles * 1.60934

    def inches_to_cm(self, inches):
        return inches * 2.54

    def feet_to_meters(self, feet):
        return feet * 0.3048

    def gallons_to_liters(self, gallons):
        return gallons * 3.78541

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def pounds_to_kg(self, pounds):
        return pounds * 0.453592

    def ounces_to_grams(self, ounces):
        return ounces * 28.3495

    def cups_to_milliliters(self, cups):
        return cups * 240

    def lakhs_to_thousands(self, lakhs):
        return lakhs * 100000

    def crores_to_millions(self, crores):
        return crores * 10000000

user_state = {}

#displaying options
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Unit Conversion", callback_data='unit_conversion')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Choose a mode:", reply_markup=reply_markup)

# Button callback handler for mode selection
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = update.effective_user.id

    if query.data == 'unit_conversion':
        user_state[user_id] = 'unit_conversion'
        await display_unit_conversion_options(query)

async def display_unit_conversion_options(query):
    keyboard = [
        [InlineKeyboardButton("Miles to Kilometers", callback_data='miles_to_km')],
        [InlineKeyboardButton("Pounds to Kilograms", callback_data='pounds_to_kg')],
        [InlineKeyboardButton("Inches to Cm", callback_data='inches_to_cm')],
        [InlineKeyboardButton("Ounces to Grams", callback_data='ounces_to_grams')],
        [InlineKeyboardButton("Fahrenheit to Celsius", callback_data='fahr_to_cel')],
        [InlineKeyboardButton("Gallons to Liters", callback_data='gallons_to_l')],
        [InlineKeyboardButton("Feet to Meters", callback_data='f_to_m')],
        [InlineKeyboardButton("Cups to Milliliters", callback_data='c_t_ml')],
        [InlineKeyboardButton("Lakhs to Thousands", callback_data='l_t_t')],
        [InlineKeyboardButton("Crores to Millions", callback_data='c_t_mi')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Choose a unit conversion:", reply_markup=reply_markup)

async def unit_conversion_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = update.effective_user.id

    if user_state.get(user_id) == 'unit_conversion':
        unit_converter = UnitConverter()

        if query.data == 'miles_to_km':
            user_state[user_id] = 'miles_to_km'
            await query.message.reply_text("Please send the number of miles to convert to kilometers.")
        elif query.data == 'pounds_to_kg':
            user_state[user_id] = 'pounds_to_kg'
            await query.message.reply_text("Please send the number of pounds to convert to kilograms.")
        elif query.data == 'inches_to_cm':
            user_state[user_id] = 'inches_to_cm'
            await query.message.reply_text("Please send the number of inches to convert to centimeters.")
        elif query.data == 'ounces_to_grams':
            user_state[user_id] = 'ounces_to_grams'
            await query.message.reply_text("Please send the number of ounces to convert to grams.")
        elif query.data == 'fahr_to_cel':
            user_state[user_id] = 'fahr_to_cel'
            await query.message.reply_text("Please send the number of Fahrenheit to convert to Celsius.")
        elif query.data == 'gallons_to_l':
            user_state[user_id] = 'gallons_to_l'
            await query.message.reply_text("Please send the number of gallons to convert to liters.")
        elif query.data == 'f_to_m':
            user_state[user_id] = 'f_to_m'
            await query.message.reply_text("Please send the number of feet to convert to meters.")
        elif query.data == 'c_t_ml':
            user_state[user_id] = 'c_t_ml'
            await query.message.reply_text("Please send the number of cups to convert to milliliters.")
        elif query.data == 'l_t_t':
            user_state[user_id] = 'l_t_t'
            await query.message.reply_text("Please send the number of lakhs to convert to thousands.")
        elif query.data == 'c_t_mi':
            user_state[user_id] = 'c_t_mi'
            await query.message.reply_text("Please send the number of crores to convert to millions.")


# Function to process user input for the conversion based on the selected option
async def handle_unit_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    # Ensure that the user has selected a conversion mode first
    if user_state.get(user_id) == 'miles_to_km':
        try:
            miles = float(text)
            unit_converter = UnitConverter()
            km = unit_converter.miles_to_km(miles)
            await update.message.reply_text(f"{miles} miles is equal to {km:.2f} kilometers.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'pounds_to_kg':
        try:
            pounds = float(text)
            unit_converter = UnitConverter()
            kg = unit_converter.pounds_to_kg(pounds)
            await update.message.reply_text(f"{pounds} pounds is equal to {kg:.2f} kilograms.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'inches_to_cm':
        try:
            inches = float(text)
            unit_converter = UnitConverter()
            cm = unit_converter.inches_to_cm(inches)
            await update.message.reply_text(f"{inches} inches is equal to {cm:.2f} centimeters.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'ounces_to_grams':
        try:
            ounces = float(text)
            unit_converter = UnitConverter()
            grams = unit_converter.ounces_to_grams(ounces)
            await update.message.reply_text(f"{ounces} ounces is equal to {grams:.2f} grams.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'fahr_to_cel':
        try:
            fahrenheit = float(text)
            unit_converter = UnitConverter()
            cel = unit_converter.fahrenheit_to_celsius(fahrenheit)
            await update.message.reply_text(f"{fahrenheit} fahrenheit is equal to {cel:.2f} celsius.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'gallons_to_l':
        try:
            gallons = float(text)
            unit_converter = UnitConverter()
            l = unit_converter.gallons_to_liters(gallons)
            await update.message.reply_text(f"{gallons} gallons is equal to {l:.2f} liters.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'f_to_m':
        try:
            f = float(text)
            unit_converter = UnitConverter()
            m = unit_converter.feet_to_meters(f)
            await update.message.reply_text(f"{f} feet is equal to {m:.2f} meters.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'c_t_m':
        try:
            cup = float(text)
            unit_converter = UnitConverter()
            milliliterss = unit_converter.cups_to_milliliters(cup)
            await update.message.reply_text(f"{cup} cups is equal to {milliliterss:.2f} milliliters.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'l_t_t':
        try:
            lak = float(text)
            unit_converter = UnitConverter()
            tho = unit_converter.lakhs_to_thousands(lak)
            await update.message.reply_text(f"{lak} lakhs is equal to {tho:.2f} thousands.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    elif user_state.get(user_id) == 'c_t_mi':
        try:
            crore = float(text)
            unit_converter = UnitConverter()
            milli = unit_converter.crores_to_millions(crore)
            await update.message.reply_text(f"{crore} crores is equal to {milli:.2f} millions.")
            user_state[user_id] = None  # Reset state
        except ValueError:
            await update.message.reply_text("Please provide a valid number.")
    else:
        await update.message.reply_text("Please select an option first using /start.")


if __name__ == "__main__":
    application = ApplicationBuilder().token('token').build()

    # Command handler for /start
    application.add_handler(CommandHandler('start', start))

    # Callback handlers for button presses
    application.add_handler(CallbackQueryHandler(button_callback, pattern='^(unit_conversion)$'))
    application.add_handler(CallbackQueryHandler(unit_conversion_callback, pattern='^(miles_to_km|pounds_to_kg|inches_to_cm|ounces_to_grams|fahr_to_cel|gallons_to_l|f_to_m|c_t_m|l_t_t|c_t_mi)$'))

    # Message handler for user input (number of miles, pounds, etc.)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_unit_input))

    # Start the bot
    application.run_polling()




